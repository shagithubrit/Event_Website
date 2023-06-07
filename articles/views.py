from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Article
from django.contrib.auth.decorators import login_required
from django import forms
# Create your views here.
def article_list(request):
    articles=Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html',{'articles':articles})

def article_details(request,slug):
    # return HttpResponse(slug)
    article=Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html',{'article':article})

def signup_view(request):
    return render(request, 'accounts/signup.html')

@login_required(login_url="/accounts/login/") # this decorator actually use to protect this view , means you can use this view unless or until you are not logged in . if user is not logged in it will redirect that url to  /accounts/login so that it non logged user redirect to login page 
def article_create(request):
    if request.method=='POST':
       form=forms.CreateArticle(request.POST,request.FILES)
       if form.is_valid():
          #save article to db
          instance=form.save(commit=False)
          instance.author=request.user
          instance.save()
          return redirect('articles:list')
    else:
     form=forms.CreateArticle()
    return render(request, 'articles/article_create.html',{'form': form})
