"""
URL configuration for festival project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('public.urls')),
    path('',include('admin_app.urls')),
    path('',include('public_user.urls')),
    path('',include('bookings.urls')),
    path('',include('organizer_app.urls')),
    path('',include('inbox.urls')),
    path('',include('complaint.urls')),
    path('',include('decorations.urls')),


   
  
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
