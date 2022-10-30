from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from environs import Env

env = Env()
env.read_env()

urlpatterns = [
    # Django admin
    path(str(env('DJANGO_ADMIN_SITE')), admin.site.urls),
    
    # Local apps
    path('', include('projects.urls')),
    path('blog/', include('blog.urls')),
    
    path(env('USER_LOGIN'), views.LoginView.as_view(), name='login'),
    path(env('USER_LOGOUT'), views.LogoutView.as_view(), name='logout')
]
