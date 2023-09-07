# Dia 2

## Dúvidas sobre Desafio 1

## Lendo e analisando texto com python

### Strings

Uma *string* é um tipo de dados Python que é tratado como texto, mesmo que contenha um número. As strings são sempre colocadas entre aspas simples `'isto é uma string'` ou aspas duplas `"isto é uma string"`.

Segundo [Allen Downey](https://penseallen.github.io/PensePython2e/08-strings.html):

>Strings não são como números inteiros, de ponto flutuante ou booleanos. Uma string é uma sequência, ou seja, uma coleção ordenada de outros valores. (...) Uma string é uma sequência de caracteres.

É possível acessar um caracter específico da string com o operador []

A expressão entre colchetes chama-se índice. O índice aponta qual caractere da sequência você quer

![](https://media.tenor.com/WOGcOj0L3vgAAAAC/caetano-veloso.gif)

```python
music = 'Terra'
music[1]
```

**Opa! o caractere na posição 1 da string music não deveria ser 'T'?**

A contagem de índices no Python começa em `0`, ou seja, o primeiro caractere é na posição 0.

A indexação é baseada na distância do ponto de partida e como o primeiro elemento está a uma distância *zero* do ponto de partida, seu índice é `0`.

```python
music[0]
```

E pra acessar o último elemento da string, você pode usar índices negativos.

```python
music[-1]
```

#### len()

len() é uma função que retorna o número de caracteres de uma string.

```python
len(music)
```

```python
another_music = 'Como 2 e 2'
len(another_music)
```

### Manipulando *strings*

#### Fatiamento de strings

Segundo [Allen Downey](https://penseallen.github.io/PensePython2e/08-strings.html):

>O operador [n:m] retorna a parte da string do “enésimo” caractere ao “emésimo” caractere, incluindo o primeiro, mas excluindo o último. Este comportamento é contraintuitivo, porém pode ajudar a imaginar os índices que indicam a parte entre os caracteres.

```python
old_music = "Avarandado"

old_music[2:5]

old_music[:5] # se omitir o primeiro número, ele começa no início da string

old_music[3:] # se omitir o último número, a fatia vai até o final da string

old_music[3:3] # Se o primeiro índice for maior ou igual ao segundo, o resultado é uma string vazia, representada por duas aspas
```

#### Concatenando strings

```python
nome = 'Caetano'
nome_completo = nome + ' ' + 'Veloso'
print(nome_completo)
```

#### Métodos de strings

```python
# lower() converte todas as letras para minusculas
nome_completo = nome_completo.lower()
print(nome_completo)

# upper() converte todas as letras para maiusculas
nome_completo = nome_completo.upper()
print(nome_completo)

# replace - substitui uma string por outra
nome_completo = nome_completo.replace('VELOSO', 'Veloso')
print(nome_completo)

# capitalize - converte a primeira letra da string para maiúscula
nome_completo = nome_completo.capitalize()

# split - divide uma string em várias strings
name1, name2 = nome_completo.split(' ')
print(name1)
print(name2)

# find - encontra a posição de uma string dentro de outra
nome_completo.find('Veloso')

# rfind - encontra a posição de uma string dentro de outra, mas começa a busca pelo final
nome_completo.rfind('V')

# count - conta quantas vezes uma string aparece dentro de outra
nome_completo.count('o')

# strip - remove os espaços em branco no início e no final da string
livro = ' Verdade Tropical             '
livro.strip()
```

#### Saiba mais sobre strings

[ABZ-Aaron](https://github.com/ABZ-Aaron) criou um repositório no Github com cheat sheets para os métdoso de strings. Lś você também encontra cheat sheets sobre listas e dicionários. 

Veja o [repositório](https://github.com/ABZ-Aaron/CheatSheets).

### Listas

Allen Downey define uma lista em Python:

>Como uma string, uma lista é uma sequência de valores. Em uma string, os valores são caracteres; em uma lista, eles podem ser de qualquer tipo. Os valores em uma lista são chamados de elementos, ou, algumas vezes, de itens.

>Há várias formas para criar uma lista; a mais simples é colocar os elementos entre colchetes ([ e ])

Listas são mutáveis. Podem conter elementos de qualquer tipo.
```python
musics = ['Lemonade', 'Halo', 'Freedom','Flawless']
years = [2000, 2019, 2016, 2013]
empty = []
multi = ['singer', 1.70, ['jay-z', 'blue ivy']]

years[1] = 2016
years

len(musics)
```

Índices de listas funcionam da mesma forma que os índices de strings

#### Métodos de listas

```python
# append - adiciona um elemento ao final de uma lista
musics.append('Formation')

# extend toma uma lista como argumento e adiciona todos os elementos
new_songs = ['Crazy in love', 'Hold up']
musics.extend(new_songs)
print(musics)

# sort - ordena uma lista
musics.sort()
musics.sort(reverse=True) # ordena a lista em ordem decrescente

musics.append('Artpop')
print(musics)

#pop - remove um elemento da lista
musics.pop() # remove o ultimo elemento da lista
print(musics)

# del - remove um elemento da lista
del musics[0]

# remove - remove um elemento da lista
musics.remove('Halo')
print(musics)

# transformar uma lista em uma string
# join - separa os elementos da lista com o separador passado
str_musics = ', '.join(musics)
print(str_musics)
```

---

- Trabalhando com ficheiros simples em python: https://programminghistorian.org/pt/licoes/trabalhando-ficheiros-texto-python
- Contagem de frequência de palavras: https://programminghistorian.org/pt/licoes/contagem-frequencia-palavras-python 
- palavras-chave em contexto com python: https://programminghistorian.org/pt/licoes/palavras-chave-contexto-usando-n-grams-python
- Controladores de fluxo
- Desafio 2