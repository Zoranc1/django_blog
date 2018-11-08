"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import get_index,read_post,edit_post,write_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_index, name='index'),
    path('write/', write_post, name='write_post'),
    path('read_post/<int:id>', read_post, name='read_post'),
    path('edit_post/<int:id>', edit_post, name='edit_post')
]