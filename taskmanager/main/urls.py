from django.urls import path
from . import views

urlpatterns = [
    path('', views.authorizations), 
    path('main', views.main),
    path('signin', views.signin)
]