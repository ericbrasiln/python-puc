# Script em Python para gerar um relatório com informações de busca
# informada pelo usuário

from datetime import datetime
import os


def get_time():
    """
    Função para retornar data e hora atual.
    Retorna três variáveis: 
    - search_time ('%Y%m%d%H%M%S')
    - date ("%d-%M-%Y")
    - time ("%H:%M:%S")
    """
    now = datetime.now()
    search_time = now.strftime('%Y%m%d%H%M%S')
    date = now.strftime("%d-%M-%Y")
    time = now.strftime("%H:%M:%S")
    return search_time, date, time


def clear_values(variable):
    """
    Função para limpar dados de variáveis que contenham
    caracteres especiais, espaços antes, depois e no meio.
    Retorna a variável limpa.

    Exemplo:
    >>> clear_values('    Hemeroteca Digital Brasileira (HDB)?    ')
    'hemeroteca_digital_brasileira_hdb'
    """
    variable = variable.lower().strip()
    variable = variable.replace(' ', '_')
    print(variable)
    special_characters = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '+', '=', '[', ']', '{', '}', '|', '\\',
                         '/', '?', '<', '>', ',', '.', ':', ';', "'", '"']
    for c in special_characters:
        variable = variable.replace(c, '_')
    return variable


def infos(user, repo_name, repo_url, search_term, total, url):
    """
    Função que recebe dados sobre uma busca e gera um relatório com
    data e hora.
    """

    search_time, date, time = get_time()
    user_clean = clear_values(user)
    repo_clean = clear_values(repo_name)
    if url == '':
        url = "Sem link para página de resultados."
    with open(f'{repo_clean}_{search_time}.txt', 'w') as f:
        f.write(f'Relatório de Busca:\n'
                f'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
                f'Nome do usuário: {user}\n'
                f'Repositório da consulta: {repo_name}\n'
                f'Link do repositório: {repo_url}\n'
                f'Termo de busca: {search_term}\n'
                f'Total de resultados retornados: {total}\n'
                f'Link da página com resultados: {url}\n'
                f'Data da busca: {date}\n'
                f'Hora da busca: {time}\n'
                )
    print('Relatório salvo com sucesso!')


user = input("Informe o nome do usuário: ")
repo_name = input("Informe o nome do repositório de busca: ")
repo_url = input("Informe a url do repositório de busca: ")
search_term = input("Informe o termo de busca: ")
total = int(input("Informe o total de resultados retornados (sempre um número inteiro): "))
results_url = input("Informe a url da página com resultados (caso não exista, deixar vazio): ")

# chamar função
infos(user, repo_name, repo_url, search_term, total, results_url)
