from ..models import Pergunta, Resposta

def obterMenuPrincipal():
    pergunta = Pergunta()
    pergunta.codigo = 1
    pergunta.titulo = "Tenho dúvida sobre minha carteira"

    resposta1 = Resposta()
    resposta1.codigo = 1
    resposta1.valor = '1'
    resposta1.descricao = "Quantas sementes eu tenho disponível?"
    resposta1.acao = "http://127.0.0.1:8000/chatbot_fiap_on_api/saldo-pontos"

    resposta2 = Resposta()
    resposta2.codigo = 2
    resposta2.valor = '2'
    resposta2.descricao = "Quando o valor renova?"
    resposta2.acao = "http://127.0.0.1:8000/chatbot_fiap_on_api/renovacao"

    resposta3 = Resposta()
    resposta3.codigo = 3
    resposta3.valor = '3'
    resposta3.descricao = "Qual o prazo para utilizar o saldo?"
    resposta3.acao = "http://127.0.0.1:8000/chatbot_fiap_on_api/prazos"

    pergunta.save()
    resposta1.save()
    resposta2.save()
    resposta3.save()

    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)
    pergunta.respostas.add(resposta3)

    return pergunta