from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from probtune.forms import QueryFormP
from probtune.models import QueryP
from vtr.models import UserProfileS
from faculty.models import UserProfileF
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
    if UserProfileF.objects.filter(user=request.user.id):
        userprofile = UserProfileF.objects.filter(user=request.user.id)
        u=1
    context_dict = {
        'userprofile': userprofile,
        'single_query': single_query,
        'popular_query': popular_query,
        'u':u
        }

    return render(request, 'probtune/query.html', context_dict) 

