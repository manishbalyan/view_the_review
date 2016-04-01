from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from vtr.forms import UserForm, UserProfileForm, QueryForm
from vtr.models import UserProfile, Query


# Create your views here.

@login_required
def index(request):
    userprofile = UserProfile.objects.filter(user=request.user.id)
    allquery = Query.objects.all().order_by('-created_at')
    popular_query = Query.objects.order_by('-views')[:5]
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
    }
    return render(request, 'vtr/index.html', context_dict)


def register(request):
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
    return render(request, 'vtr/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


@login_required
def query(request, slug):
    userprofile = UserProfile.objects.filter(user=request.user.id)
    single_query = get_object_or_404(Query, slug=slug)
    popular_query = Query.objects.order_by('-views')[:5]
    single_query.views += 1  # increment the no of views
    single_query.save()  # save it
    context_dict = {
        'single_query': single_query,
        'popular_query': popular_query,
        'userprofile': userprofile
    }
    return render(request, 'vtr/query.html', context_dict)


@login_required
def add_query(request):
    if request.method == 'POST':
        query_form = QueryForm(request.POST, request.FILES)
        if query_form.is_valid():  # is the form valid
            query_form.save(commit=True)  # yes and save to db
            return redirect(index)
        else:
            print query_form.errors  # no, display error to end user
    else:
        query_form = QueryForm()
    return render(request, 'vtr/add_query.html', {'query_form': query_form},)

def branchcs(request):
    branch_query = Query.objects.filter(tag='CSE')
    userprofile = UserProfile.objects.filter(user=request.user.id)
    popular_query = Query.objects.order_by('-views')[:5]
    context_dict = {
        'branch_query': branch_query,
        'userprofile': userprofile,
        'popular_query': popular_query,
    }
    return render(request, 'vtr/branch.html', context_dict)

def branchec(request):
    branch_query = Query.objects.filter(tag='ECE')
    userprofile = UserProfile.objects.filter(user=request.user.id)
    popular_query = Query.objects.order_by('-views')[:5]
    context_dict = {
        'branch_query': branch_query,
        'userprofile': userprofile,
        'popular_query': popular_query,
    }
    return render(request, 'vtr/branch.html', context_dict)

def branchme(request):
    branch_query = Query.objects.filter(tag='ME')
    userprofile = UserProfile.objects.filter(user=request.user.id)
    popular_query = Query.objects.order_by('-views')[:5]
    context_dict = {
        'branch_query': branch_query,
        'userprofile': userprofile,
        'popular_query': popular_query,
    }
    return render(request, 'vtr/branch.html', context_dict)

def branchee(request):
    branch_query = Query.objects.filter(tag='EE')
    userprofile = UserProfile.objects.filter(user=request.user.id)
    popular_query = Query.objects.order_by('-views')[:5]
    context_dict = {
        'branch_query': branch_query,
        'userprofile': userprofile,
        'popular_query': popular_query,
    }
    return render(request, 'vtr/branch.html', context_dict)

def branchit(request):
    branch_query = Query.objects.filter(tag='IT')
    userprofile = UserProfile.objects.filter(user=request.user.id)
    popular_query = Query.objects.order_by('-views')[:5]
    context_dict = {
        'branch_query': branch_query,
        'userprofile': userprofile,
        'popular_query': popular_query,
    }
    return render(request, 'vtr/branch.html', context_dict)

def branchce(request):
    branch_query = Query.objects.filter(tag='CE')
    userprofile = UserProfile.objects.filter(user=request.user.id)
    popular_query = Query.objects.order_by('-views')[:5]
    context_dict = {
        'branch_query': branch_query,
        'userprofile': userprofile,
        'popular_query': popular_query,
    }
    return render(request, 'vtr/branch.html', context_dict)
