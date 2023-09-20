arquivos = ['a.pdf', 'b.pdf', 'c.jpg', 'd.png', 'e.pdf']

pdfs = []

for arq in arquivos:
    if arq.endswith('.pdf'):
        pdfs.append(arq)
    else:
        continue

print(pdfs)