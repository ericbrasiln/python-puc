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

É possível acessar um caractere específico da string com o operador []

A expressão entre colchetes chama-se índice. O índice aponta qual caractere da sequência você quer

![Caetano](https://media.tenor.com/WOGcOj0L3vgAAAAC/caetano-veloso.gif)

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
musics = ['Tigresa', 'Cajuína', 'Sampa','Alegria, Alegria']
years = [2000, 1978, 1978, 1967]
empty = []
multi = ['cantor', 1.68, ['Gilberto Gil', 'Maria Bethânia', 'Gal Costa']
```

Podemos acessar os elementos de uma lista usando índices.

```python
musics[0]
```

E podemos alterar os elementos de uma lista.

```python
years[0] = 1977
years
```

Para saber o tamanho de uma lista, podemos usar a função `len()`

```python
len(musics)
```

Índices de listas funcionam da mesma forma que os índices de strings

#### Métodos de listas

```python
# append - adiciona um elemento ao final de uma lista
musics.append('Estrangeiro')

# extend toma uma lista como argumento e adiciona todos os elementos
new_songs = ['Musa Híbrida', 'Abraçaço']
musics.extend(new_songs)
print(musics)

# sort - ordena uma lista
musics.sort()
musics.sort(reverse=True) # ordena a lista em ordem decrescente

musics.append('Refavela')
print(musics)

#pop - remove um elemento da lista
musics.pop() # remove o ultimo elemento da lista
print(musics)

# del - remove um elemento da lista
del musics[0]
Halo
# remove - remove um elemento da lista
musics.remove('Abraçaço')
print(musics)

# transformar uma lista em uma string
# join - separa os elementos da lista com o separador passado
str_musics = ', '.join(musics)
print(str_musics)
```

---

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

São operadores condicionais que permitem que você execute um código se uma condição for verdadeira. Podemos entender da seguinte forma:

SE (`if`) uma condição for verdadeira, execute tal ação. SENÃO (`else`), execute outra ação. 

>Se (`if`) o semáforo **estiver vermelho** (condição 01), **pare** (ação 01). SENÃO (`else`), **siga** (ação 02).

Podemos incluir outras condições com o operador `elif` (SENÃO SE).

>Se (`if`) o semáforo **estiver vermelho** (condição 01), **pare** (ação 01). Senão, se (`elif`) **estiver amarelo** (condição 2), **reduza a velocidade** (ação 2). Senão (`else`), **siga** (ação 3).

Vejamos um exemplo:

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

A estrutura é `if` seguida da condição e dois pontos. Na linha seguinte, o bloco de código que será executado se a condição for verdadeira.

Atenção para a indentação. O Python usa a indentação para definir blocos de código.

### Criando iterações for

É fundamental entender a estrutura de iteração, realizar um loop com python.

Iterar é a capacidade de executar um bloco de instruções repetidamente.

```python
# utilizar for para percorrer a lista musics
for music in musics:
    print(f'O nome da música é {music}.')
```

#### for usando range(), len() e enumerate()

O `range()` é uma função que retorna uma sequência de números. Ela recebe três argumentos: `start`, `stop` e `step`.

Se você passar apenas um argumento, o `range()` vai considerar que esse argumento é o `stop` e vai começar a sequência em `0` e vai incrementar de `1` em `1`.

```python
for i in range(5):
    print(i)
```
A função `len()` retorna o tamanho de um objeto. Se o objeto for uma string, ela retorna o número de caracteres. Se o objeto for uma lista, ela retorna o número de elementos.

Podemos então usar o `range()` e o `len()` para percorrer uma lista.

```python
# utilizar range para percorrer um intervalo de valores
for i in range(0, len(musics)):
    print(f'A música é {musics[i]} e ela possui {len(musics[i])} letras.\n')
```

Já `enumerate()`, retorna uma tupla com o índice e o valor do elemento.
É bastante útil quando queremos acessar o índice e o valor do elemento ao mesmo tempo.

```python
for i, music in enumerate(musics):
    print(i, music)
```

Para começar a contagem do índice em `1`, basta passar o argumento `start` para a função `enumerate()`.

```python
for i, music in enumerate(musics, start=1):
    print(i, music)
```

#### continue e break

O Python possui duas palavras reservadas que permitem controlar o fluxo de execução de um loop: `continue` e `break`.

Como o próprio nome sugere, `continue` permite que você pule uma iteração do loop e continue a execução do mesmo.

Por exemplo, se não quisermos imprimir um item de uma lista que inicia com a letra `A`, podemos usar o `continue` para pular essa iteração.

```python
for music in musics:
    if music.startswith('A'):
        continue
    print(music)
```

Ou seja, o `continue` reinicia o loop sem executar o código que vem depois dele.

A palavra reservada `break` permite que você interrompa a execução do loop. Vamos ver um exemplo de encerrar um loop quando um item da lista termina com a letra `a`.

```python
for music in musics:
    if music.endswith('a'):
        break
    else:
        print(music)
```
Ou seja, o `break` interrompe o loop e o código que vem depois dele não é executado.

### while

O `while` é um loop que executa um bloco de código **enquanto** uma condição for verdadeira.

Fluxo de execução para uma instrução while:

1. Determine se a condição é verdadeira ou falsa.

1. Se for falsa, saia da instrução while e continue a execução da próxima instrução.

1. Se a condição for verdadeira, execute o corpo e então volte ao passo 1.

```python
# criar uma lista de uma contagem de 10 até 0
import time
count = 10
while count > 0:  # enquanto count for maior que 0
    print(count)  # imprima count
    time.sleep(1)  # aguarde 1 segundo
    count -= 1  # subtraia 1 de count
print("Decolar!")
```

### try / except

O `try` permite que você teste um bloco de código. E caso ele não seja executado com sucesso, você pode executar um outro bloco de código, definido pelo `except`.

```python
try:
    if len(musics) == 0:
        print('A lista de músicas está vazia.')
except:
    print('A lista não está vazia.')
```

Existem vários tipos de erros que podem ser tratados com o `try` e `except`. Veja a lista completa [aqui](https://docs.python.org/3/library/exceptions.html#bltin-exceptions).


## Desafio 2

[Contagem de Frequências de Palavras com Python](https://programminghistorian.org/pt/licoes/contar-frequencias-palavras-python)

---

[Próximo →](./dia3.ipynb)

[← Anterior](dia1.md)

[↑ Início](./README.md)