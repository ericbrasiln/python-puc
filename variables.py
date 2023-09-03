''' Script para apresentar a noção de variáveis em Pytho
'''

import pandas as pd

name = input("Digite seu nome: ")

print(f'Olá, {name}! Aproveite o curso de Python')

idade = int(input("Qual a sua idade: "))

nascimento = 2023 - idade

resposta = str(input(f"Isso quer dizer que você nasceu em {nascimento}?"))

if resposta == 'sim':
    print("Ótimo!")
elif resposta == 'não':
    print(f"Sorry! Então você nasceu em {nascimento - 1}")
else:
    print("Que resposta é essa? Tchau")
    exit()
