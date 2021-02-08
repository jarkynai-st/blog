from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog,Post
# Create your views here.


def blog_page(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request,'posts/blog.html',context)


def post_page(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'posts/post.html',context)

def blog_posts(request,blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        posts = blog.post_set.all()
        context = {'blog':blog,'post':posts}
        return render(request,'posts/posts_to_blog.html',context)
    except Blog.DoesNotExist:
        return HttpResponse('404 NOT FOUND')
