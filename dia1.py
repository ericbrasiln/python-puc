def dobrar_valor(valor=int):
    '''Dobra o valor passado como parâmetro
    >>> dobrar_valor(10)
    20
    '''
    return valor * 2


# chamada da função dobrar_valor
valor_base = int(input('Digite o valor: '))
valor_dobrado = dobrar_valor(valor_base)

print(f'o dobro do valor é {valor_dobrado}')
