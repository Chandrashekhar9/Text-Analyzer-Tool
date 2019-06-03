from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('Analyzed/', views.Analyzed, name='Analyzed'),
    path('About/', views.About, name='About'),

]
