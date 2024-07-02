
from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('register/', views.register),
    path('profile/', views.profile, name='profile'),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update)
]
