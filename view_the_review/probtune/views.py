from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.core.context_processors import csrf
from probtune.forms import QueryFormP
from probtune.models import QueryP
from vtr.models import UserProfileS
from faculty.models import UserProfileF
import hashlib, datetime, random
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count
from django_comments.models import Comment
from datetime import *
# Create your views here.


@login_required
def add_queryP(request):
    if request.method == 'POST':
        query_form = QueryFormP(request.POST, request.FILES)
        if query_form.is_valid():
            query=query_form.save(commit=False)
            query.user=request.user
            query.save()
            query_form.save_m2m()
            if UserProfileF.objects.filter(user=request.user.id):
                return redirect(probQF)
            else:
                return redirect(probQS)
        else:
           print query_form.errors

    else:
    	query_form = QueryFormP()
    return render(request, 'probtune/add_query.html', {'query_form': query_form},)


@login_required
def probQF(request):
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    allquery = QueryP.objects.all().order_by('-created_at')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title = 'ALL GENERAL QUERIES'
    context_dict = {
    'userprofile': userprofile,
    'allquery': allquery,
    'popular_query': popular_query,
    'title': title
    }
    return render(request, 'probtune/indexf.html', context_dict)

@login_required
def probQS(request):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryP.objects.all().order_by('-created_at')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title = 'ALL GENERAL QUERIES'
    context_dict = {
    'userprofile': userprofile,
    'allquery': allquery,
    'popular_query': popular_query,
    'title': title
    }
    return render(request, 'probtune/indexs.html', context_dict)

@login_required
def my_probQS(request):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryP.objects.filter(user=request.user.id).order_by('-created_at')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title = request.user.username + ' GENERAL QUERIES'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title': title
        }

    return render(request, 'probtune/indexs.html', context_dict)

@login_required
def my_probQF(request):
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    allquery = QueryP.objects.filter(user=request.user.id).order_by('-created_at')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title = request.user.username + ' GENERAL QUERIES'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title': title
        }

    return render(request, 'probtune/indexf.html', context_dict)


@login_required
def probquery(request, slug):
    single_query = get_object_or_404(QueryP, slug=slug)
    popular_query = QueryP.objects.order_by('-views')[:5]
    single_query.views += 1  # increment the no of views
    single_query.save()
    if UserProfileS.objects.filter(user=request.user.id):
        userprofile = UserProfileS.objects.filter(user=request.user.id)
        u=0
    else:
        userprofile = UserProfileF.objects.filter(user=request.user.id)
        u=1
    context_dict = {
        'userprofile': userprofile,
        'single_query': single_query,
        'popular_query': popular_query,
        'u':u
        }

    return render(request, 'probtune/query.html', context_dict) 


@login_required
def tagp(request, tag):
    allquery = QueryP.objects.filter(tags__name__in=[tag]).order_by('-created_at')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title= tag + ' Queries'
    if UserProfileS.objects.filter(user=request.user.id):
        userprofile = UserProfileS.objects.filter(user=request.user.id)
        context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title': title
        }
        return render(request, 'probtune/indexs.html', context_dict)
    else:
        userprofile = UserProfileF.objects.filter(user=request.user.id)
        context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title': title
        }
        return render(request, 'probtune/indexf.html', context_dict)



@login_required
def weekps(request):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    one_week_ago = datetime.today() - timedelta(days=7)
    allquery = QueryP.objects.filter(created_at__gte=one_week_ago).order_by('-created_at')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title= request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title':title
        }
    return render(request, 'probtune/indexs.html', context_dict)


@login_required
def monthps(request):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    one_month_ago = datetime.today() - timedelta(days=30)
    allquery = QueryP.objects.filter(created_at__gte=one_month_ago).order_by('-created_at')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title= request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title':title
        }

    return render(request, 'probtune/indexs.html', context_dict)

@login_required
def viewsps(request):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryP.objects.order_by('-views')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title= request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title':title
        }

    return render(request, 'probtune/indexs.html', context_dict)


@login_required
def commentps(request):
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryP.objects.annotate(comment_count=Count('comments')).filter(comment_count__gt=0).order_by('-comment_count')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title= request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title':title
        }

    return render(request, 'probtune/indexs.html', context_dict)


@login_required
def weekpf(request):
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    one_week_ago = datetime.today() - timedelta(days=7)
    allquery = QueryP.objects.filter(created_at__gte=one_week_ago).order_by('-created_at')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title= request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title':title
        }
    return render(request, 'probtune/indexf.html', context_dict)


@login_required
def monthpf(request):
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    one_month_ago = datetime.today() - timedelta(days=30)
    allquery = QueryP.objects.filter(created_at__gte=one_month_ago).order_by('-created_at')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title= request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title':title
        }

    return render(request, 'probtune/indexf.html', context_dict)


@login_required
def viewspf(request):
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    allquery = QueryP.objects.order_by('-views')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title= request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title':title
        }

    return render(request, 'probtune/indexf.html', context_dict)

@login_required
def commentpf(request):
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    allquery = QueryP.objects.annotate(comment_count=Count('comments')).filter(comment_count__gt=0).order_by('-comment_count')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title= request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title':title
        }

    return render(request, 'probtune/indexf.html', context_dict)


def queryp_delete(request, pk):
    queryd = get_object_or_404(QueryP, pk=pk)
    if request.method == 'POST':
        queryd.delete()
        return redirect('home')
    return render(request, 'vtr/confirm_delete.html', {'object': queryd})


def queryp_update(request, pk):
    queryu = get_object_or_404(QueryP, pk=pk)
    form = QueryFormP(request.POST or None, instance=queryu)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'vtr/update_form.html', {'form': form})

def commentp_delete(request, pk):
    commentd = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        commentd.delete()
        return redirect('home')
    return render(request, 'vtr/confirm_delete.html', {'object': commentd})


def commentp_update(request, pk):
    commentu = get_object_or_404(Comment, pk=pk)
    form = CommentDetailsForm(request.POST or None, instance=commentu)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'vtr/update_form.html', {'form': form})