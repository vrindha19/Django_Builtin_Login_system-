from django.urls import path

from .import views
from.views import login_view

urlpatterns=[
    path ('index/',views.index, name='index'),
    path('login/', login_view, name='registration/login'), 
    path('logout/', views.logout_view, name='logout'),
]