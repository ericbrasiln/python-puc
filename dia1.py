''' Script para apresentar a noção de variáveis em Python
'''
nome = 'João'  # variável do tipo string
idade = 20  # variável do tipo inteiro
altura = 1.80  # variável do tipo float

nome = input('Digite seu nome: ')  # recebemos um valor de entrada do usuário
print(
    f'Olá, {nome}! Aproveite o curso de Python!'
)  # imprimimos a mensagem na tela

idade = int(input("Qual a sua idade: "))

nascimento = 2023 - idade

resposta = str(input(f"Isso quer dizer que você nasceu em {nascimento}?"))

dif_dois_metros = 2 - altura

dif_dois_metros == altura

dif_dois_metros != altura