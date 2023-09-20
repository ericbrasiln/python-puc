
def percentage(quantidade, total):
    """
    Função que recebe uma quantidade e o total e calcula a porcentagem
    """
    resultado = (quantidade / total)*100
    return resultado

todos_arq= 270

Arq_A = percentage(12, todos_arq)
print(Arq_A)

Arq_B = percentage(4, todos_arq)
print(Arq_B)

Arq_C = percentage(50, todos_arq)
print(Arq_C)

Arq_D = percentage(30, todos_arq)
print(Arq_D)

Arq_E = percentage(20, todos_arq)
print(Arq_E)