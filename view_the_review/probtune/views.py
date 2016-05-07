"""Imports for probtune views."""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from probtune.forms import QueryFormP
from probtune.models import QueryP
from vtr.models import UserProfileS
from faculty.models import UserProfileF
from datetime import timedelta
from django.db.models import Count
from django_comments.models import Comment
from datetime import *


@login_required
def add_queryP(request):
    """View for protune add query."""
    if request.method == 'POST':
        query_form = QueryFormP(request.POST, request.FILES)
        if query_form.is_valid():
            query = query_form.save(commit=False)
            query.user = request.user
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
    """View for faculty problem."""
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
    """View for student problems."""
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
    """Student personal problems view."""
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
    """View for faculty personal problems."""
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
    """View for problem Query."""
    single_query = get_object_or_404(QueryP, slug=slug)
    popular_query = QueryP.objects.order_by('-views')[:5]
    single_query.views += 1  # increment the no of views
    single_query.save()
    if UserProfileS.objects.filter(user=request.user.id):
        userprofile = UserProfileS.objects.filter(user=request.user.id)
        u = 0
    else:
        userprofile = UserProfileF.objects.filter(user=request.user.id)
        u = 1
    context_dict = {
        'userprofile': userprofile,
        'single_query': single_query,
        'popular_query': popular_query,
        'u': u
    }

    return render(request, 'probtune/query.html', context_dict)


@login_required
def tagp(request, tag):
    """View for protune tag cloud."""
    allquery = QueryP.objects.filter(tags__name__in=[tag]).order_by('-created_at')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title = tag + ' Queries'
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
    """Weekly problem query view for students."""
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    one_week_ago = datetime.today() - timedelta(days=7)
    allquery = QueryP.objects.filter(created_at__gte=one_week_ago).order_by('-created_at')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title = request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title': title
    }
    return render(request, 'probtune/indexs.html', context_dict)


@login_required
def monthps(request):
    """Monthely problem query view for students."""
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    one_month_ago = datetime.today() - timedelta(days=30)
    allquery = QueryP.objects.filter(created_at__gte=one_month_ago).order_by('-created_at')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title = request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title': title
    }
    return render(request, 'probtune/indexs.html', context_dict)


@login_required
def viewsps(request):
    """Problem query view for students according to number of views."""
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryP.objects.order_by('-views')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title = request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title': title
    }
    return render(request, 'probtune/indexs.html', context_dict)


@login_required
def commentps(request):
    """Problem query view for students according to number of comments."""
    userprofile = UserProfileS.objects.filter(user=request.user.id)
    allquery = QueryP.objects.annotate(comment_count=Count('comments')).filter(comment_count__gt=0).order_by('-comment_count')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title = request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title': title
    }
    return render(request, 'probtune/indexs.html', context_dict)


@login_required
def weekpf(request):
    """Weekly problem query view for faculty."""
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    one_week_ago = datetime.today() - timedelta(days=7)
    allquery = QueryP.objects.filter(created_at__gte=one_week_ago).order_by('-created_at')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title = request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title': title
    }
    return render(request, 'probtune/indexf.html', context_dict)


@login_required
def monthpf(request):
    """Monthely problem query view for faculty."""
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    one_month_ago = datetime.today() - timedelta(days=30)
    allquery = QueryP.objects.filter(created_at__gte=one_month_ago).order_by('-created_at')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title = request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title': title
    }
    return render(request, 'probtune/indexf.html', context_dict)


@login_required
def viewspf(request):
    """Problem query view for faculty according to number of views."""
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    allquery = QueryP.objects.order_by('-views')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title = request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title': title
    }
    return render(request, 'probtune/indexf.html', context_dict)


@login_required
def commentpf(request):
    """Problem query view for faculty according to number of comments."""
    userprofile = UserProfileF.objects.filter(user=request.user.id)
    allquery = QueryP.objects.annotate(comment_count=Count('comments')).filter(comment_count__gt=0).order_by('-comment_count')
    popular_query = QueryP.objects.order_by('-views')[:5]
    title = request.user.username + ' Queries'
    context_dict = {
        'userprofile': userprofile,
        'allquery': allquery,
        'popular_query': popular_query,
        'title': title
    }
    return render(request, 'probtune/indexf.html', context_dict)


@login_required
def queryp_delete(request, pk):
    """Problem query delete view for user who added the query."""
    queryd = get_object_or_404(QueryP, pk=pk)
    if request.method == 'POST':
        queryd.delete()
        return redirect('home')
    return render(request, 'vtr/confirm_delete.html', {'object': queryd})


@login_required
def queryp_update(request, pk):
    """Problem query update view for user who added the query."""
    queryu = get_object_or_404(QueryP, pk=pk)
    form = QueryFormP(request.POST or None, instance=queryu)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'vtr/update_form.html', {'form': form})


@login_required
def commentp_delete(request, pk):
    """Problem comment update view for user who added the comment."""
    commentd = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        commentd.delete()
        return redirect('home')
    return render(request, 'vtr/confirm_delete.html', {'object': commentd})
