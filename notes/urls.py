"""notes URL Configuration

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
from django.conf.urls import include

from api import urls as api_urls
from user_auth import urls as auth_urls
from note import urls as notes_urls

from django.conf import settings
from django.conf.urls.static import static

from homepage.views import NoteHomePageView


urlpatterns = [

    # to authentication (login, register and profile pages)
    path("", include(auth_urls)),

    # to api
    path("api/", include(api_urls)),

    # admin url
    path("admin/", admin.site.urls),

    # notes url
    path("notes/", include(notes_urls)),

    # TinyMCE text editor
    path("tinymce/", include("tinymce.urls")),

    # Homepage url
    path("", NoteHomePageView.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
