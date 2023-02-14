from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('about/', views.about, name='about'),
    path('contacto/', views.contacto, name='contacto'),
    path('drafts/', views.post_draft_list, name='post_draft'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/like/', views.post_like, name='post_like'),
    path('post/<int:pk>/dislike/', views.post_dislike, name='post_dislike'),
    re_path(r'^post/(?P<pk>\d+)/comment/$',
            views.add_comment_to_post, name='add_comment_to_post'),
    path('post/approve<int:pk>/', views.comment_approve, name='comment_approve'),
    path('post/remove/<int:pk>', views.comment_remove, name='comment_remove'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
]
