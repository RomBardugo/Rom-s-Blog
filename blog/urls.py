from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name='main-page'),
    path("posts", views.posts, name='posts-page'),
    path("posts/<slug:slug>", views.show_post, name="post-detail-page")
]
