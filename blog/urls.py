from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    # path('', views.post_list, name='post_list'),

    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    # path('<int:id>/', views.post_detail, name='post_detail'),

    path('create/', views.PostCreateView.as_view(), name='create_post_view'),
    # path('create/', views.create_post_view, name='create_post_view'),

    path('<int:pk>/update/', views.UpdatePostView.as_view(), name='update_post'),
    # path('<int:id>/update/', views.update_post_view, name='update_post'),

    path('<int:pk>/delete/', views.DeletePostView.as_view(), name='delete_post'),
    # path('<int:id>/delete/', views.delete_post_view, name='delete_post'),
]