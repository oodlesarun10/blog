from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

# Create your views here.
def home(request):
    return render(request,'home/home.html')
   # return HttpResponse("this is home")



def about(request):
   # return HttpResponse("this is about")
   return render(request, 'home/about.html')

def contact(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
      #  print(name,email,phone,content)
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<10:
            messages.error(request,'Please fill the form correctly')
        else:
            contact=Contact(name = name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"Your form is submit ")
    return render(request, 'home/contact.html')

def search(request):
    query=request.GET['query']
    allPostsTitle=Post.objects.filter(title__icontains=query)
    allPostsContent=Post.objects.filter(content__icontains=query)
    allPosts=allPostsTitle.union(allPostsContent)
    params={'allPosts':allPosts,'query':query}
    return render(request,'home/search.html',params)
    #return HttpResponse("This is search")

def handleSignup(request):
    if request.method=='POST':
        username = request.POST['username']
      #  print(username,'ajhjdaahj')
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username)>12 :
            messages.error(request,'Username must be under 12 characters')
            return redirect('home')
        if not username.isalnum():
            messages.error(request, 'Username must contain letter and numbers')
            return redirect('home')
        if pass1!=pass2:
            messages.error(request, 'Password must match')
            return redirect('home')


        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        print(myuser,'adjkhuahjk')
        myuser.save()
        messages.success(request,"Your account is created successfully")
        return redirect('home')

    else:
        return HttpResponse('404 Not Found')


def handleLogin(request):
    if request.method=='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)
        #if user is there
        if user is not None:
            login(request,user)
            messages.success(request, "Logged In successfully")
            return redirect('home')
        #if user is none or not there
        else:
            messages.error(request, "Invalid credentials ,Please try again")
            return redirect('home')

    return HttpResponse('404 Not Found')


def handleLogout(request):
   # if request.method=='POST':
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')




