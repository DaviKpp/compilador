
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
linha = 0
coluna = 0
while scout < len(r):
    temp = scout

    #Operador
    constant.simplecrawler(r, sentinela, scout, arrToken, linha, coluna)

    #Inteiros
    sentinela, scout = constant.crawler(r, constant.inteiro, sentinela, scout, 'inteiro', arrToken)
    
    #Id
    sentinela, scout = constant.crawler(r, constant.alfabeto, sentinela, scout, 'id', arrToken)
    
    if scout == temp:
        
        
        
        scout = scout + 1
f = open('lexico.txt', 'w')
for x in arrToken:
    
    if x.erro == 1:
        print("Erro léxico")
    else:
        if re.match(constant.palavrarese, x.lexema):
            x.tipo = 'palavra-reservada'
        f.write('<'+ x.lexema + ',' + x.tipo + '>' + '\n')