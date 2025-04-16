from django.shortcuts import render, redirect ,get_object_or_404
from .forms import *
from .models import *

def createpost(request):
    if request.method == 'POST':
        form = Createpost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('createpost')  # or wherever you want
    else:
        form = Createpost()
    return render(request, 'user/createpost.html', {'posts': form})
def viewpost(request):
    profiles=Post.objects.all() 
    return render(request,'user/viewpost.html',{'profiles':profiles})
def delet(request,pk):
    obj=get_object_or_404(Post,pk=pk)
    obj.delete()
    return redirect('viewpost')
def update(request, pk):
    obj = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = Createpost(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('viewpost')  
    else:
        posts = Createpost(instance=obj)  

    return render(request, 'user/createpost.html', {"posts": posts})
