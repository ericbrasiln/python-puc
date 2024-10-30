"""Criar um script que gere um relatório de pesquisa em texto simples, contendo (a partir dos dados inseridos pelo usuário):

- Nome do usuário
- Nome do Repositório de pesquisa
- url do Repositório de pesquisa
- Data e hora da busca
- Termo de busca
- Total de resultados
- url do resultado
"""

# importar bibliotecas: datetime
import datetime

data = datetime.datetime.now()
search_time = data.strftime('%Y%m%d_%H%M%S')


# solicitar dados ao usuário
nome = input("Digite seu nome: ")
repositorio = input("Digite o nome do repositório: ")
#url = input("Digite a url do repositório: ")
#termo = input('Digite o termo da busca: ')
#total = input('Digite o total de resultados: ')
#url_res = input('Digite a url da página de resultados: ')

print(data)

with open(f'{repositorio}_{search_time}.txt', 'w') as f:
    f.write('Relatório de busca.\n'
            f'Nome do usuário: {nome}\n'
            f'Nome do Repositório: {repositorio}\n' 

            )
