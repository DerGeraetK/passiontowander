from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('about', views.about, name='blog_about'),
    path('post-list', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('all-posts/', views.all_posts, name='blog_all_posts'),
    path('upload_image/', views.upload_image_view, name='upload_image'),
    path('upload_video/', views.upload_video_view, name='upload_video'),
    path('imprint/', views.imprint, name='imprint'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms-and-conditions'),
]
