def dobrar_valor(valor=int):
    """Dobra o valor passado como parâmetro
    >>> dobrar_valor(10)
    20
    """
    return valor * 2


# chamada da função dobrar_valor
valor_base = int(input('Digite o valor: '))
valor_dobrado = dobrar_valor(valor_base)

print(f'o dobro do valor é {valor_dobrado}')

# create a list
list_names = []
# input the names of the students
for i in range(1, 6):
    name = input(f'Digite o nome do estudante número {i}: ')
    list_names.append(name)

# loop na lista musics e salva cada item em um arquivo txt
for estudante in list_names:
    # abre o arquivo txt
    file = open(estudante + '.txt', 'w')  # w = write
    # escreve o valor usando format
    file.write(str
               (f'O nome do/a estudante é {estudante}\
                e ele possui {len(estudante)} letras.')
               )
    file.close()  # fecha o arquivo
