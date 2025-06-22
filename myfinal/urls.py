"""
URL configuration for myfinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views as auth_views
from myapp.views import custom_logout_view
from rest_framework.authtoken.views import obtain_auth_token
from django.http import JsonResponse
def health_check(request):
    return JsonResponse({
        "status": "ok", 
        "message": "Django is working",
        "method": request.method,
        "path": request.path
    })
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', custom_logout_view, name='logout'),
    path('', include("myapp.urls")),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('health/', health_check),
]
