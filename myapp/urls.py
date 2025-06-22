from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'menu-items', views.MenuItemViewSet, basename='menuitem')

urlpatterns = [
    path('api/', include(router.urls)), 
    path('api/logout/', views.LogoutView.as_view(), name='api-logout'),
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('book/', views.book,name="book"),
    path('menu-items/', views.menu_view,name="menu"),
    path('menu-items/add/', views.menu_item_create, name='menu_item_create'),
    path('menu-items/<int:pk>/edit/', views.menu_item_update, name='menu_item_update'),
    path('menu-items/<int:pk>/delete/', views.menu_item_delete, name='menu_item_delete'),
    path('menu_item/<pk>', views.menu_item,name="menu_item"),
    path('booked-slots/', views.get_booked_slots, name='booked_slots'),
]