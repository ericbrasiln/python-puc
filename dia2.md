# Dia 2

## Dúvidas sobre Desafio 1

## Funções

Podemos criar nossas próprias funções para executar tarefas específicas. Para isso, usamos a palavra reservada `def` seguida do nome da função e dos parênteses. 

```python
def imprimir_saudacao(pessoa):
    print(f'Olá, {pessoa}! Como vai?')
```
Essa função se chama `imprimir_saudacao` e recebe um argumento `pessoa`. O argumento é uma variável que será utilizada dentro da função.

Para executar a função, basta chamá-la pelo nome e passar o argumento.

```python
imprimir_saudacao('Maria')
```

Mas e se eu quiser utilizar o retorno da função em uma variável?

```python
def dobrar_valor(valor):
    return valor * 2
```
 
Agora podemos utilizar o retorno da função em uma variável.

```python
dobro = dobrar_valor(5)
print(dobro)
```

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

## Listas

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

## Controladores de fluxo

[Python Basics 2](https://hub.binder.constellate.org/user/ithaka-tdm-notebooks-mb3z11hb/notebooks/python-basics-2.ipynb) de [Nathan Kelber](http://nkelber.com/) e Ted Lawless

### Tipos de controle de fluxo


|Declaração|Significado|Condição de execução|
|---|---|---|
|`if`|se|se a condição for atendida|
|`elif`|senão se|se nenhuma condição anterior for atendida *e* esta condição for atendida|
|`else`|senão|se nenhuma condição for atendida (nenhuma condição é fornecida para uma instrução `else`)|
|`while`|enquanto|enquanto a condição for verdadeira|
|`for`|para|executar em um loop um quantidade de vezes|
|`try`|tentar|tente isso e execute o código `except` se ocorrer um erro|

### if / elif / else

Operações condicionais

```python
number = int(input('Digite um número: '))
```

```python
if number > 0:
    print('positive')
elif number < 0:
    print('negative')
else:
    print('zero')
```

### Criando iterações for

É fundamental entender a estrutura de iteração, realizar um loop com python.

Iterar é a capacidade de executar um bloco de instruções repetidamente.

```python
# utilizar for para percorrer a lista musics
for music in musics:
    length_music = len(music)
    print(f'A música é {music} e ela possui {length_music} letras.\n')
```

```python
# utilizar range para percorrer um intervalo de valores
for i in range(0, len(musics)):
    print(f'A música é {musics[i]} e ela possui {len(musics[i])} letras.\n')
```
```python
# create a list
list_names = []
# input the names of the students
for i in range(1,6):
    name = input(f'Digite o nome do estudante número {i}: ')
    list_names.append(name)
```

```python
# loop na lista musics e salva cada item em um arquivo txt
for music in musics:
    # abre o arquivo txt
    file = open(music + '.txt', 'w') # w = write
    # escreve o valor usando format
    file.write(str(f'A música é {music} e ela possui {len(music)} letras.\n'))
    file.close() # fecha o arquivo
```

#### for usando range(), len() e enumerate()

```python
```

#### continue e break

- A continue statement immediately restarts the loop.

- A break statement immediately exits the loop.

```python
```

### while

Fluxo de execução para uma instrução while:

1. Determine se a condição é verdadeira ou falsa.

1. Se for falsa, saia da instrução while e continue a execução da próxima instrução.

1. Se a condição for verdadeira, execute o corpo e então volte ao passo 1.

```python
# criar uma lista de uma contagem de 10 até 0
import time
count = 10
while count > 0:
    print(count)
    time.sleep(1)
    count -= 1
print("Ok, Ladies, now let's get in formation!")
```

### try / except

```python
```




- Desafio 2