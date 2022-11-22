from django.shortcuts import render
from rest_framework.decorators import api_view
from .business import principal, saldoPontos
from .serializers import PerguntaSerializer
from django.http.response import JsonResponse

# Create your views here.
@api_view(['GET'])
def obterPrincipal(request):
    menuInicial = principal.obterMenuPrincipal()
    menuInicial_serializer = PerguntaSerializer(menuInicial)
    resp = JsonResponse(menuInicial_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp    

@api_view(['GET'])
def obterSaldoPontos(request):
    menuSaldoPontos = saldoPontos.obterSaldoPontos()
    menuSaldoPontos_serializer = PerguntaSerializer(menuSaldoPontos)
    resp = JsonResponse(menuSaldoPontos_serializer.data,safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp    
    