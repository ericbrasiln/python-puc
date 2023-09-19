"""
Script que recebe o nome de uma pessoa e a idade.
Imprime na tela uma mensagem de saudação (que inclui o nome)
e informa quantos anos ela terá em 2030.
"""

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
idade_2030 = idade + 7

print(f'Olá, {nome}. Você terá {idade_2030} anos em 2030.')
