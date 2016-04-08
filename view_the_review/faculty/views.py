from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from faculty.forms import UserForm, UserProfileFormF
from vtr.models import QueryS
from hostel.models import QueryH
from faculty.models import UserProfileF
from django.db.models import Q


@login_required
def index(request):
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    if (userprofile[0].department == 'WARDEN'):
    	allquery = QueryH.objects.all().order_by('-created_at')
    	popular_query = QueryH.objects.order_by('-views')[:5]
    else:
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
    return render(request, 'faculty/index.html', context_dict)


def registerF(request):
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileFormF(data=request.POST)
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
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
            profile.save()

            return render(request, 'vtr/login.html')
            
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileFormF()

    # Render the template depending on the context.
    return render(request, 'faculty/register.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def query(request, slug):
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    if (userprofile[0].department == 'WARDEN'):
    	single_query = get_object_or_404(QueryH, slug=slug)
    	popular_query = QueryH.objects.order_by('-views')[:5]
    else:
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

    return render(request, 'faculty/query.html', context_dict)



@login_required
def branch(request, branch_name):
    userprofile = UserProfileF.objects.filter(user=request.user.id)
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

    return render(request, 'faculty/index.html', context_dict)  


@login_required
def my_queryf(request):
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    if (userprofile[0].department == 'WARDEN'):
    	allquery = QueryH.objects.filter(user=request.user.id).order_by('-created_at')
    	popular_query = QueryH.objects.order_by('-views')[:5]
    else:
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

    return render(request, 'faculty/index.html', context_dict)  




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
        return render(request,'faculty/index.html', variables)
    else:
        return render(request,'faculty/search.html', variables)


