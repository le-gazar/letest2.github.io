"""Appli_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from HomePage.views import home,josue,essai,detail,search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',  home, name='home'),
    path('josue/', josue, name='josue'),
    path('essai/', essai, name="essai"),
    path("", include("app_auth.urls")),
    path('article/<int:id_article>',detail,name='detail'),
    path('article/recherche',search,name='search')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

