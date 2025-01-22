"""
URL configuration for app project.

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
from django.urls import include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


from . import views



urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    
    #login, utilizando o que retorna pronto do django
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view() , name='logout'),
   
    #authentication
    path('api/v1/', include('authentication.urls')),
    
    #home front
    path('',views.home, name='home'),
    #apps front
    path('api/', include('rpas.urls')),
    path('api/', include('rpa_log_successes.urls')),
    path('api/', include('rpa_log_errors.urls')),

]
