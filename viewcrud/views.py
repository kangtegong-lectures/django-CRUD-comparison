from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog

def welcome(request):
    return render(request, 'viewcrud/index.html')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'viewcrud/funccrud.html', {'blogs':blogs})

def create(request):
    if request.method =='POST':
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = NewBlog()
        return render(request, 'viewcrud/new.html', {'form':form})

def update(request, pk):

    # 어떤 블로그를 수정할지 블로그 객체를 갖고오기
    blog = get_object_or_404(Blog, pk = pk)
    
    # 해당하는 블로그 객체 pk에 맞는 입력공간
    form = NewBlog(request.POST, instance=blog)
    
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'viewcrud/new.html', {'form':form})

    
def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')

