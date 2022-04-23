
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
while scout < len(r):
    #Inteiros
    sentinela, scout = constant.crawler(r, constant.inteiro, sentinela, scout, 'inteiro', arrToken)
    
    #Id
    sentinela, scout = constant.crawler(r, constant.alfabeto, sentinela, scout, 'id', arrToken)
    scout = scout + 1

