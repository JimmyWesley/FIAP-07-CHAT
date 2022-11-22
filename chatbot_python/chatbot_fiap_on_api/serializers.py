from dataclasses import fields
from rest_framework import serializers

from .models import Pergunta, Resposta

class RespostaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Resposta
        fields = '__all__'

class PerguntaSerializer(serializers.ModelSerializer):

    respostas = RespostaSerializer(many=True)

    class Meta:

        model = Pergunta
        fields = '__all__'