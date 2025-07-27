from django.core.exceptions import ObjectDoesNotExist
# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.models import Post


# Create your views here.

def post_list(request):
    AllPost = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': AllPost})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

# def post_detail(request, id):
#     try:
#         post = Post.objects.get(id=id)
#         # return render(request, 'blog/post_detail.html', {'post': post})
#     except(ObjectDoesNotExist):
#         post = None
#         print('page does not exist')
#         # return HttpResponse('Page does not exist')
#     return render(request, 'blog/post_detail.html', {'post': post})



