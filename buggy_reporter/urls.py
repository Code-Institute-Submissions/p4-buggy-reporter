"""buggy_reporter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from web_viewer.views import show_bug_viewer, index, create_bugs, edit_bugs

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('bugs/', show_bug_viewer),
    path('bugs/new/', create_bugs),
    path('bugs/edit/<id>', edit_bugs)
]
