from django.urls import path, include
from . import views
from django.contrib import admin

app_name = 'app'
#x=admin.site.urls

urlpatterns = [
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('', views.home, name='home'),
    path('home/', views.admin_home, name='admin_home'),
    path('marketplace/', views.placements, name='placements'),
    path('marketplace/<placement_slug>/', views.placement_detail, name='placement-detail'),

    path('my-bids/', views.bid_summary, name='bid-summary' ),
    path('confirm-bids/', views.confirm_bids, name='confirm-bids'),

    path('dashboard/', views.about, name='dashboard'),
    path('createbiddings/', views.createbiddings, name='createbiddings'),
    path('confirmbiddings/', views.confirmbiddings, name='confirmbiddings'),
    path('confirmbid/<id>/', views.confirmbid, name='confirmbid'),
    path('confirmed/<id>/', views.confirmed, name='confirmed'),


]
