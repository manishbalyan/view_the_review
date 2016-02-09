from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from vtr.forms import UserForm
# from vtr.models import Post
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from vtr.forms import UserForm, UserProfileForm, QueryForm
from vtr.models import UserProfile, Query



def get_popular_query():
    popular_query = Query.objects.order_by('-views')[:5]
    return popular_query
# Create your views here.


@login_required
def index(request):
    userprofile = UserProfile.objects.filter(user=request.user)
    singlequery = Query.objects.all().order_by('-created_at')
    context_dict = {
        'userprofile': userprofile,
        'singlequery': singlequery,
        'popularquery': get_popular_query()
    }
    return render(request, 'vtr/index.html', context_dict)

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
    # Attempt to grab information from the raw form information.
    # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
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
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            # Now we save the UserProfile model instance.
            profile.save()
            # Update our variable to tell the template registration was successful.
            registered = True
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    # Render the template depending on the context.
    return render_to_response(
            'vtr/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)


def query(request, query_url):
    single_query = get_object_or_404(Query, title=query_url.replace('_', ' '))
    popular_query = Query.objects.order_by('-views')[:5]
    single_query.views += 1  # increment the no of views
    single_query.save()# save it
    t = loader.get_template('vtr/query.html')
    c = Context({'single_query': single_query, 'popular_query': popular_query, })
    return HttpResponse(t.render(c))

def add_query(request):
    context = RequestContext(request)
    if request.method == 'POST':
        query_form = QueryForm(request.POST, request.FILES)
        if query_form.is_valid():  # is the form valid
            query_form.save(commit=True)  # yes and save to db
            return redirect(index)
        else:
            print query_form.errors  # no, display error to end user
    else:
        query_form = QueryForm()
    return render_to_response('vtr/add_query.html', {'query_form': query_form}, context)