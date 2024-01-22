from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup' ), 
    path('signin', views.signin, name='signin' ),  
    path('signout', views.signout, name='signout' ),
    path('inicio', views.inicio, name='inicio'),
    path('inicio/coroa', views.coroa, name='coroa'),
    path('inicio/forma', views.forma, name='forma'),
    path('inicio/bloco', views.bloco, name='bloco'),
    path('inicio/coroa/results', views.coroa_view, name='coroa_view'),  
    path('inicio/forma/results', views.forma_view, name='forma_view'),  
    path('inicio/bloco/results', views.bloco_view, name='bloco_view'),
    path('accounts', include('django.contrib.auth.urls'))
]   