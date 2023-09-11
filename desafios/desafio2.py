
def clean_text(text):
    """
    Recebe um texto e o coloca em minúsculas, elimina os caracteres que não são alfanuméricos e retorna uma lista de palavras.
    """
    import re
    text = text.lower()
    text = re.compile(r'\W+', re.UNICODE).split(text)
    new_list = []
    for x in text:
        if len(x) > 2:
            new_list.append(x)
    return new_list


def word_list_to_freq_dict(wordlist):
    """
    Dada uma lista de palavras, retorna um dicionário de pares palavra-frequência.
    """
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))


def sort_freq_dict(freqdict):
    """
    Ordena um dicionário de pares palavra-frequência em ordem decrescente de frequência.
    """
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux


# abrir arquivo quereres.txt
with open('quereres.txt', 'r') as f:
    text = f.read()
    # lower case 
    text = text.lower()
    wordlist =  clean_text(text)
    dictionary = word_list_to_freq_dict(wordlist)
    sorteddict = sort_freq_dict(dictionary)

    for s in sorteddict:
        print(str(s))