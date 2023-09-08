# Dia 1 

## Apresentação geral

- Objetivos gerais
- Estrutura do curso
- Metodologia

## Introdução à Python

- O que é Python e por que é usado?
- Como instalar o Python?
- Ambiente de trabalho no VSCode

## Conceitos básicos de programação em Python

### O temido terminal! 

Podemos e comumente vamos executar comandos e scripts diretamente através de linhas de comando no terminal.

```
python3 <nome-do-script>.py

``` 

Ou ainda, você pode acessar o python em seu terminal e executar comandos de forma interativa executando o comando:

```
python3
```

Vamos explorar um pouco o terminal e o python interativo.

### Variáveis

Traduzido de [Variables](https://melaniewalsh.github.io/Intro-Cultural-Analytics/02-Python/04-Variables.html) Melanie Walsh.

As variáveis são um dos blocos de construção fundamentais do Python. Uma variável é como um pequeno contêiner onde você armazena valores e dados, como nomes de arquivos, palavras, números, coleções de palavras e números e muito mais.

#### Definindo variáveis

O nome da variável apontará para um valor que você "atribui" a ele. Você pode pensar em atribuição de variável como colocar um valor "dentro" da variável, como se a variável fosse uma pequena caixa 🎁

Você atribui variáveis com um sinal de igual `=`. Em Python, um único sinal de igual `=` é o "operador de atribuição". Um sinal de igual duplo `==` é o sinal de igual "real".

```python
# criar uma variável
nome = 'Maria'
#imprimir o valor da variável
print(nome)
```
#### Nomeando variáveis

Os nomes das variáveis podem ser tão longos ou curtos quanto você quiser e podem incluir:
- letras maiúsculas e minísculas (A-Z)
- dígitos (0-9)
- underscores (_)

No entanto, os nomes das variáveis * não podem * incluir:
- ❌ outras pontuações (-.!?@)
- ❌ spaces ( )
- ❌ uma palavra reservada do Python

Variáveis claras e nomeadas com precisão irão:

* tornar seu código mais legível (para você e para outras pessoas)
* reforçar sua compreensão do Python e do que está acontecendo no código
* esclarecer e fortalecer seu pensamento

Para maiores informações veja o [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

#### Palavras-chave do Python
Retirado de [Pense Python](https://penseallen.github.io/PensePython2e/02-vars-expr-instr.html) de Allen Downey, capítulo 2.

O interpretador usa palavras-chave para reconhecer a estrutura do programa e elas não podem ser usadas como nomes de variável.

O Python 3 tem estas palavras-chave:

```
and         del         from        None        True
as          elif        global      nonlocal    try
assert      else        if          not         while
break       except      import      or          with
class       False       in          pass        yield
continue    finally     is          raise
def         for         lambda      return
```

Você não precisa memorizar essa lista. Na maior parte dos ambientes de desenvolvimento, as palavras-chave são exibidas em uma cor diferente; se você tentar usar uma como nome de variável, vai perceber.

#### Redefinindo variáveis

As variáveis não são fixas, é possível atribuir novos valores a uma varivável que já havia sido definida anteriormente.

```python
nome = 'Eric'
print(nome)
```

### Tipos de Dados

Existem quatro tipos essenciais de dados Python com diferentes poderes e capacidades:

- Strings (texto)
- Inteiros (números inteiros)
- Floats (números decimais)
- Booleans (verdadeiro / falso)


|Tipo | Explicação | Exemplo |
|---|---|---|
|integer|número inteiro| -3, 0, 2, 534|
|float|número decimal | 6.3, -19.23, 5.0, 0.01|
|string|texto| 'Hello world', '1700 butterflies', '', '1823'|
|boolean|Verdadeiro ou Falso| True/False|

Você pode verificar o tipo de dados de qualquer valor usando a função `type ()`.

```python
type(nome)
```

### Operadores Aritméticos

[Python Basics 1](https://hub.binder.constellate.org/user/ithaka-tdm-notebooks-mb3z11hb/notebooks/python-basics-1.ipynb) de [Nathan Kelber](http://nkelber.com/) e Ted Lawless

|Operador| Operação| Exemplo | Resultado |
|---|----|---|---|
|\*\*| Potência| 3 ** 3 | 27 |
|%| Resto da divição| 34 % 6 | 4 |
|/| Divisão | 30 / 6 | 5|
|//| Divisão inteira | 27 // 6 | 4 |
|\*| Multiplicação | 7 * 8 | 56 |
|-| Subtração | 18 - 4| 14|
|+| Adição | 4 + 3 | 7 |

### Operadores relacionais

[Python Basics 2](https://hub.binder.constellate.org/user/ithaka-tdm-notebooks-mb3z11hb/notebooks/python-basics-2.ipynb) de [Nathan Kelber](http://nkelber.com/) e Ted Lawless

|Operador|Significado|
|---|---|
|==|Igual|
|!=|diferente|
|<|Menor que|
|>|Maior que|
|<=|Menor ou igual que|
|>=|Maior ou igual que|

### Operadores Booleanos (and/or/not)

[Python Basics 2](https://hub.binder.constellate.org/user/ithaka-tdm-notebooks-mb3z11hb/notebooks/python-basics-2.ipynb) de [Nathan Kelber](http://nkelber.com/) e Ted Lawless

- and

```True and True = True```

- or

|Expressão|Avaliação|
|---|---|
|True or True|True|
|True or False|True|
|False or True|True|
|False or False|False|

### print() input() e format()

Vejamos três funções básicas do Python que nos ajudarão a interagir com o usuário e a imprimir valores na tela.

Funções em Python são blocos de código que executam uma tarefa específica. As funções podem receber valores de entrada (argumentos) e retornar valores de saída. Elas são reconhecidas por terem um nome seguido de parênteses.

Para imprimir na tela um valor devemos utilizar a função `print()`.

Para receber um valor de entrada do usuário, usamos a função `input()`.

Usamos format() para formatar strings.

```python
print(nome)

new_name = input('Digite seu nome: ')
print(new_name)

print(f'Olá, {new_name}! Como vai?')
```

## Desafio 1: *Seu primeiro script*

Monte um script que receba o nome de uma pessoa e sua idade. Imprima na tela uma mensagem de saudação (que inclua o nome) e informe quantos anos ela terá em 2030.

Tente utilizar os operadores aritméticos e as funções print(), format() e input().
