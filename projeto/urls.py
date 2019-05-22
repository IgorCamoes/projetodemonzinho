"""projeto URL Configuration

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
from django import views
from demonday import views
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('perfil', views.perfil, name='perfil'),
    url(r'perfil/(?P<username>[a-zA-Z0-9]+)$', views.pega_o_user, name='usuario'),
    path('jogos/', views.paginaJogos, name='jogos'),
    path('login/', LoginView.as_view(template_name='login.html'), name='loginn'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('feed/', views.feed, name='feed'),
    path('user/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)