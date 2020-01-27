from django.shortcuts import render,HttpResponse
from .models import Post

# Create your views here.
def blogHome(request):
    allPosts=Post.objects.all()
    print(allPosts)
    context={'allPosts':allPosts}
    return render(request,'blog/blogHome.html',context)



def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    print(post)
    context={'post':post}
    return render(request, 'blog/blogPost.html',context)
    # return HttpResponse('this is blogpost :{slug}')
