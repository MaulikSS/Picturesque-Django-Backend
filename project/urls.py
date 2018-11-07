from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path("login/", views.loginView, name="login"),
    path("register/", views.registerView, name="register"),
    path("home/", views.homePage, name="homepage"),
    path("post/<int:pk>/", views.postDetail, name="detail"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("post/<int:pk>/like/", views.like, name="like"),
    path("post/<int:pk>/comment/", views.uploadComment, name="comment"),
    path("post/upload/", views.uploadPost, name="uploadPost"),
    path("logout/", views.logout_view, name="logout")
]