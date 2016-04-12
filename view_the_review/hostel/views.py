from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from hostel.forms import QueryFormH
from hostel.models import QueryH
from vtr.models import UserProfileS
from faculty.models import UserProfileF
from faculty.views import index as indexf
# Create your views here.


@login_required
def add_queryH(request):
    if request.method == 'POST':
        query_form = QueryFormH(request.POST, request.FILES)
        if query_form.is_valid():
            query=query_form.save(commit=False)
            query.user=request.user
            query.save()
            query_form.save_m2m()
            if UserProfileF.objects.filter(user=request.user.id):
                return indexf(request)
            else:
                return redirect(hostelQ)
        else:
           print query_form.errors

    else:
    	query_form = QueryFormH()
    return render(request, 'hostel/add_query.html', {'query_form': query_form},)


@login_required
def hostelQ(request):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryH.objects.all().order_by('-created_at')
    popular_query = QueryH.objects.order_by('-views')[:5]
    title = 'ALL HOSTEL QUERIES'
    context_dict = {
    'userprofile': userprofile,
    'allquery': allquery,
    'popular_query': popular_query,
    'title': title
    }
    return render(request, 'hostel/index.html', context_dict)

@login_required
def my_hostelQ(request):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryH.objects.filter(user=request.user.id).order_by('-created_at')
    popular_query = QueryH.objects.order_by('-views')[:5]
    title = request.user.username + ' HOSTEL QUERIES'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title': title
        }

    return render(request, 'hostel/index.html', context_dict)

@login_required
def hostelquery(request, slug):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    single_query = get_object_or_404(QueryH, slug=slug)
    popular_query = QueryH.objects.order_by('-views')[:5]
    single_query.views += 1  # increment the no of views
    single_query.save()
    context_dict = {
        'userprofile': userprofile,
        'single_query': single_query,
        'popular_query': popular_query
        }

    return render(request, 'hostel/query.html', context_dict) 

