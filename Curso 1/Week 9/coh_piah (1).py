
from os import remove
import re
from typing import overload

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def calcula_assinatura(texto): # JÁ TÁ TUDO CERTO.... CARÁI!
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    #  chamar todas as "funções de separação" e armazenar seus resultados para uso repetitivo antes das contas

    # Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    
    #     somar todos os caracteres do texto que não sejam espaços ou pontuação
    for letra in texto:
        letterCounter=0
        if letra!=" " and letra!="," and letra!="." and letra!="?" and letra!="!" and letra!=";" and letra!=":" and letra!="/" and letra!="-" and letra!="+" and letra!="_":
            letterCounter+=1

    #     contar a quantidade de palavras no texto
    wordCounter=0
    for sentenca in separa_sentencas(texto):
        for frase in sentenca:
            for palavra in frase:
                wordCounter+=1

    #     dividir o número de caracteres pela quantidade de palavras

    wal = letterCounter / wordCounter # wal é o tamanho médio da palavra

    # Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.

    #     contar a quantidade total de palavras 
    
    wordCounter=0
    for sentenca in separa_sentencas(texto):
        for frase in sentenca:
            for palavra in frase:
                wordCounter+=1
    
    #     contar a quantidade de palavras diferentes
    differentWords=[]
    for sentenca in separa_sentencas(texto):
        for frase in sentenca:
            for palavra in frase:
                if palavra not in differentWords:
                    differentWords.append(palavra)
    len(differentWords)

    #     Dividir quantidade de palavras diferentes pela quantidade total de palavras

    ttr = len(differentWords) / wordCounter # ttr éType_token

    # Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras. hlr

    #     Contar a quantidade de palavras utilizadas um única vez

    textCopy = texto.split()
    uniqueWords=[]
    for i in textCopy:
        repeatedWord = False
        for j in textCopy:
            if i!=j:
                if textCopy.index(i) == textCopy.index(j):
                    repeatedWord = True
        if repeatedWord == False:
            uniqueWords.append(textCopy.index(i))
    len(uniqueWords)

    #     Contar a quantidade total de palavras

    wordCounter=0
    for sentenca in separa_sentencas(texto):
        for frase in sentenca:
            for palavra in frase:
                wordCounter+=1

    #     Dividir  quantidade de palavras utilizadas um única vez pela quantidade total de palavras

    hlr=len(uniqueWords) / wordCounter # hlr é Hapax Legomana

    # Tamanho médio de sentença: Média simples do número de caracteres por sentença.  sal

    #     somar todos os caracteres do texto que não sejam espaços ou pontuação

    for letra in texto:
        letterCounter=0
        if letra!=" " and letra!="," and letra!="." and letra!="?" and letra!="!" and letra!=";" and letra!=":" and letra!="/" and letra!="-" and letra!="+" and letra!="_":
            letterCounter+=1

    #     contar a quantidade de sentenças no texto

    sentencaCounter=0
    for sentenca in separa_sentencas(texto):
        sentencaCounter+=1

    #     dividir o número de caracteres do texto pela quantidade de sentenças

    sal=letterCounter / sentencaCounter

    # Complexidade de sentença: Média simples do número de frases por sentença. sac

    #     contar a quantidade de sentenças no texto

    sentencaCounter=0
    for sentenca in separa_sentencas(texto):
        sentencaCounter+=1

    #     contar a quantidade de frases no texto

    fraseCounter=0
    for sentenca in separa_sentencas(texto):
        for frase in sentenca:
            fraseCounter+=1

    #     dividir a quantidade de sentenças no texto pela quantidade de frases no texto

    sac = fraseCounter / sentencaCounter

    # Tamanho médio de frase: Média simples do número de caracteres por frase. pal

    #     somar todos os caracteres do texto que não sejam espaços ou pontuação

    for letra in texto:
        letterCounter=0
        if letra!=" " and letra!="," and letra!="." and letra!="?" and letra!="!" and letra!=";" and letra!=":" and letra!="/" and letra!="-" and letra!="+" and letra!="_":
            letterCounter+=1

    #     contar a quantidade de frases no texto

    fraseCounter=0
    for sentenca in separa_sentencas(texto):
        for frase in sentenca:
            fraseCounter+=1

    #     dividir a quantidade de caracteres no texto pela quantidade de frases no texto    

    pal = letterCounter /  fraseCounter

    as_a = [wal, ttr, hlr, sal, sac, pal]

    return as_a


def compara_assinatura(as_a, as_b): # JÁ TÁ TUDO CERTO.... CARÁI!
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    
    # grau de similaridade = somatório(módulo(subtração(cada traço linguístico de cada texto))) / 6

    summation=0
    for parameter in range(5):
        summation+=abs(as_a[parameter] - as_b[parameter])

    return summation / 6 


#ass_cp assinatura de referencia retornada pela função le_assinatura
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''    
    # Calcular a assinatura de cada texto
    listaAssinaturas = []
    for texto in textos:
        listaAssinaturas.append(calcula_assinatura(texto))
    
    # Compara cada assinatura calculada com a assinatura de referencia
    listaGrauSimilaridade = []
    for assinatura in listaAssinaturas:
        listaGrauSimilaridade.append(compara_assinatura(assinatura, ass_cp))
    
    maiorSimilaridade = min(listaGrauSimilaridade)

    # retorna o número do texto com a maior probabilidade de ter o mesmo autor da assinatura de referencia
    return listaGrauSimilaridade.index(maiorSimilaridade)+1

listaTextos = le_textos()
assinaturaReferencia = le_assinatura()
textoComMaiorSimilaridade = avalia_textos(listaTextos,assinaturaReferencia)

print(f"O autor do texto {textoComMaiorSimilaridade} está infectado com COH-PIAH")
