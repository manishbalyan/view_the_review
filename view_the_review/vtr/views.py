from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.core.context_processors import csrf
from vtr.forms import UserForm, UserProfileFormS, QueryFormS, SearchForm
from vtr.models import UserProfileS, QueryS
from faculty.models import UserProfileF
from django.db.models import Q
from faculty.views import index as indexf
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone


# Create your views here.

def home(request):
    if UserProfileS.objects.filter(user=request.user.id):
        return index(request)
    elif UserProfileF.objects.filter(user=request.user.id):
        userprofile = UserProfileF.objects.filter(user=request.user.id)

#       if userprofile[0].department == 'ADMINISTRATION':
#           return administration.views.index(request)
#       else:
        return indexf(request)
    else:
        return render(request, 'vtr/home.html')




@login_required
def index(request):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryS.objects.all().order_by('-created_at')
    popular_query = QueryS.objects.order_by('-views')[:5]
    branch = ['CSE','IT','ECE','ME','CE','EN']
    title='All QUERIES'
    context_dict = {
    'userprofile': userprofile,
    'allquery': allquery,
    'popular_query': popular_query,
    'branch': branch,
    'title': title
    }
    return render(request, 'vtr/index.html', context_dict)


def registerS(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileFormS(data=request.POST)
        # If the two forms are valid...
        args['form'] = user_form
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            activation_key = hashlib.sha1(salt+email).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            user.set_password(user.password)
            user.save()
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            # Now we save the UserProfile model instance.
            profile = UserProfileS(user=user, activation_key=activation_key, key_expires=key_expires)
            profile.save()

             # Send email with activation key
            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/vtr/confirm/%s" % (username, activation_key)

            send_mail(email_subject, email_body, 'balyan05.manish@gmail.com', [email], fail_silently=False)
            return render(request, 'vtr/home.html')
            
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileFormS()

    # Render the template depending on the context.
    return render(request, 'vtr/register.html', {'user_form': user_form, 'profile_form': profile_form})


def register_confirm(request, activation_key):
    # check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('/home')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(UserProfileS, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('vtr/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.user
    user.is_active = True
    user.save()
    return render_to_response('vtr/confirm.html')

@login_required
def query(request, slug):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    single_query = get_object_or_404(QueryS, slug=slug)
    popular_query = QueryS.objects.order_by('-views')[:5]
    branch = ['CSE','IT','ECE','ME','CE','EN']
    single_query.views += 1  # increment the no of views
    single_query.save()
    context_dict = {
        'userprofile': userprofile,
        'single_query': single_query,
        'popular_query': popular_query,
        'branch': branch
        }

    return render(request, 'vtr/query.html', context_dict)


@login_required
def add_queryS(request):
    if request.method == 'POST':
        query_form = QueryFormS(request.POST, request.FILES)

        if query_form.is_valid():# is the form valid
            query= query_form.save(commit=False)
            if UserProfileF.objects.filter(user=request.user.id):
                query.branch=UserProfileF.objects.only('department').get(user=request.user).department
            else:
                query.branch=UserProfileS.objects.only('branch').get(user=request.user).branch
            query.user=request.user
            query.save()
            query_form.save_m2m()

            
            return redirect(home)
        else:
            print query_form.errors  # no, display error to end user
    else:
        query_form = QueryFormS()
    return render(request, 'vtr/add_query.html', {'query_form': query_form},)


@login_required
def branch(request, branch_name):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryS.objects.filter(branch= branch_name).order_by('-created_at')
    popular_query = QueryS.objects.order_by('-views')[:5]
    branch = ['CSE','IT','ECE','ME','CE','EN']
    title= branch_name + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'branch': branch,
        'title': title
        }

    return render(request, 'vtr/index.html', context_dict)  


@login_required
def my_query(request):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryS.objects.filter(user=request.user.id).order_by('-created_at')
    popular_query = QueryS.objects.order_by('-views')[:5]
    branch = ['CSE','IT','ECE','ME','CE','EN']
    title= request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'branch': branch,
        'title':title
        }

    return render(request, 'vtr/index.html', context_dict)  




def search_page(request):
    form = SearchForm()
    Query = []
    show_results = False
    if request.GET.has_key('query'):
        show_results = True
        query = request.GET['query'].strip()
        if query:
            keywords = query.split()
            q = Q()
            for keyword in keywords:
                q = q & Q(title__icontains=keyword)
            form = SearchForm({'query' : query})
            Query = QueryS.objects.filter(q)[:10]
    variables = {
        'form': form,
        'Query': Query,
        'show_results': show_results,
        }
    if request.GET.has_key('ajax'):
        return render(request,'vtr/index.html', variables)
    else:
        return render(request,'vtr/search.html', variables)

