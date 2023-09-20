ies = []

with open('ies.txt', 'r') as file:
    for linha in file:
        linha = linha.lower().strip()
        ies.append(linha)

print(ies)