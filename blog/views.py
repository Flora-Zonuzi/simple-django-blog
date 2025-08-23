from http.client import HTTPResponse

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import NewPostForm
from blog.models import Post

from django.views import generic
from django.urls import reverse_lazy


from django.contrib import messages


# Create your views here.

class PostListView(generic.ListView):
    # model = Post
    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-date_modified')
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# def post_list(request):
#     AllPost = Post.objects.filter(status='pub').order_by('-date_modified')
#     # AllPost = Post.objects.filter(status='pub') # faghat publish ha ro neshon bede
#     # AllPost = Post.objects.all() # in hamaro neshon mide khat bala filter kardim
#     return render(request, 'blog/post_list.html', {'posts': AllPost})

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# def post_detail(request, id):
#     post = get_object_or_404(Post, id=id)
#     return render(request, 'blog/post_detail.html', {'post': post})
# def post_detail(request, id):
#     try:
#         post = Post.objects.get(id=id)
#         # return render(request, 'blog/post_detail.html', {'post': post})
#     except(ObjectDoesNotExist):
#         post = None
#         print('page does not exist')
#         # return HttpResponse('Page does not exist')
#     return render(request, 'blog/post_detail.html', {'post': post})

class PostCreateView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/create_post_view.html'
    success_url = reverse_lazy('post_list')
    # success_url='/blog/'

# def create_post_view(request):
# #------------------------check konim har kodom chie
#     # print(request.method)
#     # print(request.POST.get('title'))
#     # print(request.POST.get('text'))
# #--------------------------------------------------
#     if request.method == 'POST':
#         form = NewPostForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             return redirect('create_post_view')
#         # else: # chon or None dar form ezafe kardim else ro bardashtam
#         #     print(form.errors)
#     else:
#         form = NewPostForm()
#         return render(request, 'blog/create_post_view.html', {'form': form})
#     #----------------------------------------------------------------
#     # if request.method == 'POST':
#     #     Post.objects.create(title=request.POST.get('title'),
#     #                         text=request.POST.get('text'),
#     #                         author=User.objects.all()[0],
#     #                         status='pub')
#     #     # return redirect('post_list') #  bad az ezafe kardan post bere safhe post list name dadim chonkr url mikhad na html
#     #     # return render (request, 'blog/create_post_view.html', {'message': 'Post created successfully'}) #moshkeli ke dare bad az refresh safhe momkene dbare post kone behtare redirect bezanim
#     #     return redirect('create_post_view') # be khodesh redirect kardam ke safhe refresh she va hamin ja bemone
#     # else:
#     #     form = NewPostForm()
#     #     return render(request, 'blog/create_post_view.html')
#     #----------------------------------------------
#     # if request.method == 'POST':
#     #     post_title = request.POST.get('title')
#     #     post_text = request.POST.get('text')
#     #     post_author = User.objects.all()[0] #yek user be tor etefaghi [0=avalin] ra felan dar nazar begirad
#     #     Post.objects.create(title=post_title, text=post_text, author=post_author, status='pub') # yek method baraye zakhore model
#     # else:
#     #     print('GET request zadi')
#     # return render(request, 'blog/create_post_view.html')

class UpdatePostView(generic.UpdateView):
    model = Post # mesle create faghat inja esme model ham migim khali nafereste
    form_class = NewPostForm
    template_name = 'blog/create_post_view.html'
    success_url = reverse_lazy('post_list')
#
# def update_post_view(request, id):
#     post = get_object_or_404(Post, id=id)
#     form = NewPostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
#     return render(request, 'blog/create_post_view.html', context={'form': form})
#-----------------------------------------------------------khobe vali jadid save mikone
    # if request.method == 'POST':
    #     form = NewPostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('post_list')
    #     else:
    #         print(form.errors)
    # else:
    #     post=get_object_or_404(Post, id=id)
    #     form = NewPostForm(instance=post)
    # return  render (request, 'blog/create_post_view.html', context={'form': form})
#-------------------------------------------------------------ebtedai
    # post = get_object_or_404(Post, id=id)
    # form = NewPostForm(instance = post)
    # return render(request, 'blog/create_post_view.html', context={'form':form})

class DeletePostView(generic.DeleteView):
   model = Post
   template_name = 'blog/delete_post.html'
   success_url = reverse_lazy('post_list')

# def delete_post_view(request, id):
#     post = get_object_or_404(Post, id=id)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#     return render (request, 'blog/delete_post.html', context={'post': post})