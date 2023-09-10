# linha de comentário contém um # no início
# comentários são ignorados pelo computador
# geralmente iniciamos um script com comentários que explicam o que ele faz

# importamos as bibliotecas que serão necessárias
import datetime  # biblioteca para trabalhar com datas e horas

# cada linha abaixo é uma instrução que será executada pelo computador
# na ordem em que aparecem

hora_atual = datetime.datetime.now()  # criamos uma variável para armazenar a hora atual
nome = input('Digite seu nome: ')  # recebemos um valor de entrada do usuário
print(
    f'Olá, {nome}! São {hora_atual.hour} horas e {hora_atual.minute} minutos.'
)  # imprimimos a mensagem na tela
