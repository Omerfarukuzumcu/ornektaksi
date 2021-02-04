from django.shortcuts import render,redirect
from .forms import CommentForm
from django.contrib import messages
from .models import Comment
# Create your views here.

def index(request):
    form = CommentForm(request.POST or None)
    comments = Comment.objects.all()
    context = {
        "comments":comments
    }
    if request.method == "POST":
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_content=comment_content)
        newComment.save()

        return redirect("index")
    return render(request, "index.html",context)

def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')