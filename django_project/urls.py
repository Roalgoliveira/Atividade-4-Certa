"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from appDoRodrigo import views

urlpatterns = [
  path('', views.home, name="home"),
  path('jog_h/', views.adicionar_jogador_h),
  path('jog_h/update/<id>', views.update_jogador_h),
  path('jog_h/delete/<id>', views.delete_jogador_h),
  path('jog_top/', views.adicionar_jogador_top),
  path('jog_top/update/<id>', views.update_jogador_top),
  path('jog_top/delete/<id>', views.delete_jogador_top),
  path('admin/', admin.site.urls)
]
