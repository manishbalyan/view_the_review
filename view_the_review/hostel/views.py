"""Imports related to hostel views."""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from hostel.forms import QueryFormH
from hostel.models import QueryH
from vtr.models import UserProfileS
from faculty.models import UserProfileF
from faculty.views import index as indexf
from datetime import datetime, timedelta
from django.db.models import Count
from datetime import *


@login_required
def add_queryH(request):
    """Hostel query add view."""
    if request.method == 'POST':
        query_form = QueryFormH(request.POST, request.FILES)
        if query_form.is_valid():
            query = query_form.save(commit=False)
            query.user = request.user
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
    """View for all hostel queries."""
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
    """User personal hostel queries view."""
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
    """View for hostel queries."""
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
    """View for tag cloud fir hostel."""
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryH.objects.filter(tags__name__in=[tag]).order_by('-created_at')
    popular_query = QueryH.objects.order_by('-views')[:5]
    branch = ['CSE', 'IT', 'ECE', 'ME', 'CE', 'EN']
    title = tag + ' Queries'
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
    """View for weekly hostel query."""
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    one_week_ago = datetime.today() - timedelta(days=7)
    allquery = QueryH.objects.filter(created_at__gte=one_week_ago).order_by('-created_at')
    popular_query = QueryH.objects.order_by('-views')[:5]
    branch = ['CSE', 'IT', 'ECE', 'ME', 'CE', 'EN']
    title = request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'branch': branch,
        'title': title
    }
    return render(request, 'hostel/index.html', context_dict)


@login_required
def monthh(request):
    """View for monthely hostel query."""
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    one_month_ago = datetime.today() - timedelta(days=30)
    allquery = QueryH.objects.filter(created_at__gte=one_month_ago).order_by('-created_at')
    popular_query = QueryH.objects.order_by('-views')[:5]
    branch = ['CSE', 'IT', 'ECE', 'ME', 'CE', 'EN']
    title = request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'branch': branch,
        'title': title
    }
    return render(request, 'hostel/index.html', context_dict)


@login_required
def viewsh(request):
    """View for hostel query according to number of views."""
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryH.objects.order_by('-views')
    popular_query = QueryH.objects.order_by('-views')[:5]
    branch = ['CSE', 'IT', 'ECE', 'ME', 'CE', 'EN']
    title = request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'branch': branch,
        'title': title
    }
    return render(request, 'hostel/index.html', context_dict)


@login_required
def commenth(request):
    """View for hostel query according to number of comments."""
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryH.objects.annotate(comment_count=Count('comments')).filter(comment_count__gt=0).order_by('-comment_count')
    popular_query = QueryH.objects.order_by('-views')[:5]
    branch = ['CSE', 'IT', 'ECE', 'ME', 'CE', 'EN']
    title = request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'branch': branch,
        'title': title
    }
    return render(request, 'hostel/index.html', context_dict)


@login_required
def queryh_delete(request, pk):
    """Hostel query delete view for user who added the query."""
    queryd = get_object_or_404(QueryH, pk=pk)
    if request.method == 'POST':
        queryd.delete()
        return redirect('home')
    return render(request, 'vtr/confirm_delete.html', {'object': queryd})


@login_required
def queryh_update(request, pk):
    """Hostel query update view for user who added the query."""
    queryu = get_object_or_404(QueryH, pk=pk)
    form = QueryFormH(request.POST or None, instance=queryu)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'vtr/update_form.html', {'form': form})


@login_required
def commenth_delete(request, pk):
    """Hostel comment update view for user who added the comment."""
    commentd = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        commentd.delete()
        return redirect('home')
    return render(request, 'vtr/confirm_delete.html', {'object': commentd})
