from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('tes2/', views.tes2),
    path('tes3/', views.tes3),
    path('tes4/', views.tes4)
]
