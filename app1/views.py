from django.shortcuts import render ,redirect
from django.http import HttpResponse
from app1.models import Post,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import SignUpModel
from django.urls import reverse
from django.contrib.auth.hashers import check_password,make_password

#from .serializers import PostSerializer , CategorySerializer
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .forms import PostForm

# Create your views here.
def home(request):
    posts=Post.objects.all()
    cats=Category.objects.all()
    
    data={
        'posts':posts,
        'cats':cats
    }
    return render(request,"app1/index.html",data)

def post_detail (request,url):
    post=Post.objects.get(url=url)
    cats=Category.objects.all()
    #return HttpResponse(f"Requested URL:{url}")
    return render(request,"app1/post.html",{'post':post,'cats':cats})

def category(request,url):
    cat=Category.objects.get(url=url)
    cats=Category.objects.all()
    posts=Post.objects.filter(cat_id=cat)
    return render(request,"app1/category.html",{'cat':cat,'posts':posts,'cats':cats})

def profile(request):
    cats=Category.objects.all()
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request,"app1/profile.html",{'cats':cats})


def user_login(request):
    error=""
    cats=Category.objects.all()
    if request.method == "POST":
        u=request.POST["email"]
        p=request.POST["password"]
        user=authenticate(username=u, password=p)
        if user:
            login(request,user)
            error="no"
        else:
            error="yes"
    context={'error':error,'cats':cats}
    return render(request,"app1/user_login.html",context)

def registration(request):
    cats=Category.objects.all()
    error=""
    if request.method == "POST":
        fn=request.POST["first_name"]
        ln=request.POST["last_name"] 
        em=request.POST["email"]
        pwd=request.POST["password"]
        country=request.POST["country"]
        state=request.POST["state"]
        city=request.POST["city"]
        try:
            user=User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            SignUpModel.objects.create(user=user,country=country,state=state,city=city)
            user.save()
            error="no"
        except:
            error="yes"
    context={'error':error,'cats':cats}
    return render(request,"app1/registration.html",context)



def profile_edit(request):
    cats=Category.objects.all()
    error=""
    user=request.user
    try:
        profile = SignUpModel.objects.get(user=user)
        if request.method == "POST":
            fn=request.POST['first_name']
            ln=request.POST['last_name']
            em=request.POST['email']
            country=request.POST['country']
            state=request.POST['state']
            city=request.POST['city']
            
            profile.user.first_name=fn
            profile.user.last_name=ln
            profile.user.username=em
            profile.country=country
            profile.state=state
            profile.city=city
            try:
                profile.save()
                profile.user.save()
                error="no"
            except:
                error="yes"
        context={'error':error,'profile':profile,'cats':cats}
        return render(request,"app1/profile_edit.html",context)
    except SignUpModel.DoesNotExist:
        return HttpResponse("Employee profile not found.")

def change_password(request):
    error=""
    cats=Category.objects.all()
    user=request.user
    if request.method == "POST":
        c=request.POST['currentpassword']
        n=request.POST['newpassword']
        cn=request.POST['confirmpassword']
        try:
            if user.check_password(c):
                if n==cn:
                    user.set_password(n)
                    user.save()
                    error="no"
                else:
                    error="cp"
            else:
                error="not"
        except:
            error="yes"
    return render(request,"app1/change_password.html",{'error':error,'cats':cats})

def logout_user(request):
    logout(request)
    return redirect('user_login')




def add_post(request,url=None):
    error=''
    if url is not None:
        category=Category.objects.get(url=url)

    else:
        category=None
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            if category:
                post.cat_id=category
            post.save()
            error='no'
        else:
            error='yes'
           
    else:
        form=PostForm()
    return render(request,"app1/add_post.html",{'form':form,'error':error})


def delete_post(request,post_id):
    error=''
    pi=Post.objects.get(post_id=post_id)
    pi.delete()
    error='no'
    #return HttpResponse("Deleted Succefull")
    return render(request,"app1/category.html",{'error':error})



def update_post(request,post_id):
    error=''
    po=Post.objects.get(pk=post_id)
    
    if request.method == "POST":
        form=PostForm(request.POST,instance=po)
        if form.is_valid():
            form.save()
            error='no'
        else:
            error='yes'
    else:
        form=PostForm(instance=po)
    return render(request,"app1/update_post.html",{'form':form,'error':error})
