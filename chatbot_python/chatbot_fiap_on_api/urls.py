from django.urls import path
from . import views

urlpatterns = [
    path('principal', views.obterPrincipal, name='menu-principal'),
    path('saldo-pontos', views.obterSaldoPontos, name='saldo-pontos'),
    path('renovacao', views.obterSaldoPontos, name='renovacao'),
    path('prazos', views.obterSaldoPontos, name='prazos'),
]