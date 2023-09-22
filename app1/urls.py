from django.urls import path,include
from . import views
#from .views import PostListView,PostDetailView,CategoryListView,CategoryDetailView
from rest_framework.decorators import action
urlpatterns = [
    path('',views.home,name='home'),
    path('post/<slug:url>/',views.post_detail,name='post'),
    path('category/<slug:url>/',views.category,name='category'),
    path('profile/',views.profile,name="profile"),
    path('user_login/',views.user_login,name="user_login"),
    path('registration/',views.registration,name="registration"),
    path('profile_edit/',views.profile_edit,name="profile_edit"),
    path('change_password/',views.change_password,name="change_password"),
    path('logout_user/',views.logout_user,name="logout_user"),
    path('add_post/',views.add_post,name='add_post'),
    path('delete/<int:post_id>/',views.delete_post,name="delete_post"),
    path('update_post/<int:post_id>/',views.update_post,name='update_post'),
    # These Are the Api urls Path
    #path('category/',CategoryListView.as_view(),name='category'),
    #path('posts/',PostListView.as_view(),name='posts'),
    #path('posts/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    #path('category/<int:pk>',CategoryDetailView.as_view(),name='category-detail'),
]
