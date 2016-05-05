from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.core.context_processors import csrf
from hostel.forms import QueryFormH
from hostel.models import QueryH
from vtr.models import UserProfileS
from faculty.models import UserProfileF
from faculty.views import index as indexf
import hashlib, datetime, random
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count
from django_comments.models import Comment
from datetime import *
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


@login_required
def tagh(request, tag):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryH.objects.filter(tags__name__in=[tag]).order_by('-created_at')
    popular_query = QueryH.objects.order_by('-views')[:5]
    branch = ['CSE','IT','ECE','ME','CE','EN']
    title= tag + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'branch': branch,
        'title': title
        }

    return render(request, 'hostel/index.html', context_dict)


@login_required
def weekh(request):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    one_week_ago = datetime.today() - timedelta(days=7)
    allquery = QueryH.objects.filter(created_at__gte=one_week_ago).order_by('-created_at')
    popular_query = QueryH.objects.order_by('-views')[:5]
    branch = ['CSE','IT','ECE','ME','CE','EN']
    title= request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'branch': branch,
        'title':title
        }
    return render(request, 'hostel/index.html', context_dict)


@login_required
def monthh(request):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    one_month_ago = datetime.today() - timedelta(days=30)
    allquery = QueryH.objects.filter(created_at__gte=one_month_ago).order_by('-created_at')
    popular_query = QueryH.objects.order_by('-views')[:5]
    branch = ['CSE','IT','ECE','ME','CE','EN']
    title= request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'branch': branch,
        'title':title
        }

    return render(request, 'hostel/index.html', context_dict)


@login_required
def viewsh(request):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryH.objects.order_by('-views')
    popular_query = QueryH.objects.order_by('-views')[:5]
    branch = ['CSE','IT','ECE','ME','CE','EN']
    title= request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'branch': branch,
        'title':title
        }

    return render(request, 'hostel/index.html', context_dict)


@login_required
def commenth(request):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryH.objects.annotate(comment_count=Count('comments')).filter(comment_count__gt=0).order_by('-comment_count')
    popular_query = QueryH.objects.order_by('-views')[:5]
    branch = ['CSE','IT','ECE','ME','CE','EN']
    title= request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'branch': branch,
        'title':title
        }

    return render(request, 'hostel/index.html', context_dict)