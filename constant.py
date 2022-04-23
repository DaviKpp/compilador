import constant
import re

inteiro = "^[-+]?[0-9]+$"
alfabeto = "[a-zA-Z]"

class Token:
    def __init__(self, lexema, tipo, linha, coluna, pos, erro):
        self.lexema = lexema
        self.tipo = tipo
        self.linha = linha
        self.coluna = coluna
        self.pos = pos
        self.erro = erro
      
    
    def printToken(self):
        print("Lexema: " + str(self.lexema) +
        "\nTipo: " + str(self.tipo) + 
        "\nLinha: " + str(self.linha) + 
        "\nColuna: " + str(self.coluna) + 
        "\nPosição: " + str(self.pos) +
        "\nErro: " + str(self.erro))

def crawler(arq, regex, sentinela, scout, tipo, arrToken):
    linha = 0
    coluna = 0
    pos = 0
    if re.match(regex, arq[scout]):
        sentinela = scout
        print(arq[scout])
        scout = scout + 1
        while scout < len(arq) and re.match(regex, arq[scout]):
            print(arq[scout])
            scout = scout + 1
        if scout == len(arq):
            scout = scout - 1 
        if not re.match("\s", arq[scout]):
            print("Erro Léxico!")
            lexema = ''.join([str(elem) for elem in arq[sentinela:scout]])
            token = Token(lexema, tipo, linha, coluna, pos, 1)
            token.printToken()
            arrToken.append(token)
            pos = pos + 1
            return sentinela, scout
        else:
            print("Token Criado!")
            lexema = ''.join([str(elem) for elem in arq[sentinela:scout]])
            token = Token(lexema, tipo, linha, coluna, pos, 0)
            token.printToken()
            arrToken.append(token)
            pos = pos + 1
            return sentinela, scout
    else:
        return sentinela, scout