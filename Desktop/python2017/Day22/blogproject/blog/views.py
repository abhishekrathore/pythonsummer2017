from django.http import HttpResponse
from django.template import loader
from .models import Post,Comment,User
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt



def posts(request):
    template = loader.get_template("home.html")
    all_posts = Post.objects.all().order_by('-published_at')
    context = {"all_posts":all_posts}
    return HttpResponse(template.render(context,request))


def user(request):
    template = loader.get_template("user.html")
    return HttpResponse(template.render())


def post(request,post_id):
    template = loader.get_template("post.html")
    print(post_id)
    post = Post.objects.get(id=post_id)
    users = User.objects.all()
    comments = Comment.objects.filter(post_id=post_id)
    context = {"post":post,"users":users,"comments":comments}
    return HttpResponse(template.render(context,request))

def author(request,author_id):
    template = loader.get_template("author.html")
    author = User.objects.get(id=author_id)
    posts = Post.objects.filter(user_id=author_id)
    context = {"author":author,"posts":posts}
    return HttpResponse(template.render(context,request))

@csrf_exempt
def comment_submit(request,post_id):
    author = request.POST.get('author')
    text = request.POST.get('text')
    comment = Comment(content=text,user_id=author,post_id=post_id)
    comment.save()
    return redirect('post',post_id)


@csrf_exempt
def create_user(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    picture = request.FILES.get('file')
    user = User(username=username,email=email,picture=picture)
    user.save()
    return redirect('home')