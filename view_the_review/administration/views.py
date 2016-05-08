"""Import for admin views."""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from vtr.models import QueryS
from hostel.models import QueryH
from faculty.models import UserProfileF
from probtune.models import QueryP
from datetime import datetime


@login_required
def index(request):
    """View for addmin index page."""
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    allquery = QueryP.objects.all().order_by('-created_at')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title = 'All GENERAL QUERIES'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title': title
    }
    return render(request, 'administration/index.html', context_dict)


@login_required
def hostel(request):
    """View for hostel query in admin module."""
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    allquery = QueryH.objects.all().order_by('-created_at')
    popular_query = QueryH.objects.order_by('-views')[:5]
    title = 'All HOSTEL QUERIES'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title': title
    }
    return render(request, 'administration/indexh.html', context_dict)


@login_required
def academic(request):
    """View for acadmic query in admin module."""
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    allquery = QueryS.objects.all().order_by('-created_at')
    popular_query = QueryS.objects.order_by('-views')[:5]
    title = 'All ACADEMIC QUERIES'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title': title
    }
    return render(request, 'administration/indexs.html', context_dict)


@login_required
def Pquery(request, slug):
    """View for popular query in admin."""
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    single_query = get_object_or_404(QueryP, slug=slug)
    popular_query = QueryP.objects.order_by('-views')[:5]
    single_query.views += 1  # increment the no of views
    single_query.save()
    context_dict = {
        'userprofile': userprofile,
        'single_query': single_query,
        'popular_query': popular_query
    }
    return render(request, 'administration/query.html', context_dict)


@login_required
def Aquery(request, slug):
    """View for admin query in admin module."""
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    single_query = get_object_or_404(QueryS, slug=slug)
    popular_query = QueryS.objects.order_by('-views')[:5]
    single_query.views += 1  # increment the no of views
    single_query.save()
    context_dict = {
        'userprofile': userprofile,
        'single_query': single_query,
        'popular_query': popular_query
    }
    return render(request, 'administration/query.html', context_dict)


@login_required
def Hquery(request, slug):
    """View for hostel query in admin module."""
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    single_query = get_object_or_404(QueryH, slug=slug)
    popular_query = QueryH.objects.order_by('-views')[:5]
    single_query.views += 1  # increment the no of views
    single_query.save()
    context_dict = {
        'userprofile': userprofile,
        'single_query': single_query,
        'popular_query': popular_query
    }
    return render(request, 'administration/query.html', context_dict)
