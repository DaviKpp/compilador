
from asyncio.windows_events import NULL
import re
from unittest.mock import sentinel
import constant

nome_arq = input("Digite o nome do arquivo: ")
arq = open(nome_arq)
r = arq.read()
sentinela = 0
scout = 0
arrToken = []
espaco = " "
r = r + espaco
linha = 1
coluna = 1
while scout < len(r):
    temp = scout
    if(r[scout]== '\n'):
        linha = linha + 1
        coluna = 1
    #Operador
    constant.simplecrawler(r, sentinela, scout, arrToken, linha, coluna)

    #Inteiros
    sentinela, scout = constant.crawler(r, constant.inteiro, sentinela, scout, 'inteiro', arrToken, linha, coluna)

    #Literal
    sentinela, scout = constant.crawler(r, constant.literal, sentinela, scout, 'literal', arrToken, linha, coluna)
    
    #Id
    sentinela, scout = constant.crawler(r, constant.alfabeto, sentinela, scout, 'id', arrToken, linha, coluna)


    if scout == temp:
        if not re.match(constant.delimitador, r[scout]):
            print("Erro léxico!\n"+
            "Linha:" + str(linha) +
            "\nColuna: " + str(coluna))
        scout = scout + 1
    else:
        coluna = coluna+1
f = open('lexico.txt', 'w')
for x in arrToken:
    
    if x.erro == 1:
        print("Erro léxico!\n"+
        "Linha:" + str(x.linha) +
        "\nColuna: " + str(x.coluna))
    else:
        if re.match(constant.palavrarese, x.lexema):
            x.tipo = 'palavra-reservada'
        f.write('<'+ x.lexema + ',' + x.tipo + '>' + '\n')