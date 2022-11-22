from os import O_ACCMODE
from ..models import Pergunta, Resposta

def obterSaldoPontos():

    
    pergunta = Pergunta()
    pergunta.codigo = 2
    pergunta.titulo = "O seu saldo é vitalício, pode usar quando quiser."

   

    resposta2 = Resposta()
    resposta2.codigo = 22
    resposta2.valor = '1'
    resposta2.descricao = "Voltar para o Menu"
    resposta2.acao = "http://127.0.0.1:8000/chatbot_fiap_on_api/principal"

    pergunta.save()
    resposta2.save()
    
    pergunta.respostas.add(resposta2)
    
    return pergunta