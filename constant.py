import constant
import re

inteiro = "^[-+]?[0-9]+$"
alfabeto = "['a-zA-Z]"
palavrarese = "(void|main|printf|for|while|do|if|else|int|float|char|double|long|break)"
delimitador = "[\s|\n|+|-|,|{|}|(|)|;|/|=|*|<|>]"
deli = "[\s|(|)|;|+|=|{|}|<|>]"
operador = "[+|-|=|*|/|<|>]"
literal = "'[a-zA-Z]*'"

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
        "\nErro: " + str(self.erro))

def crawler(arq, regex, sentinela, scout, tipo, arrToken, linha, coluna):
    pos = 0
    if re.match(regex, arq[scout]):
        sentinela = scout
        scout = scout + 1
        while scout < len(arq) and re.match(regex, arq[scout]):
            scout = scout + 1
        if scout == len(arq):
            scout = scout - 1 
        if not re.match(deli, arq[scout]):
            lexema = ''.join([str(elem) for elem in arq[sentinela:scout]])
            token = Token(lexema, tipo, linha, coluna, pos, 1)
            arrToken.append(token)
            pos = pos + 1
            return sentinela, scout
        else:
            lexema = ''.join([str(elem) for elem in arq[sentinela:scout]])
            token = Token(lexema, tipo, linha, coluna, pos, 0)
            arrToken.append(token)
            pos = pos + 1
            return sentinela, scout
    else:
        return sentinela, scout

def faztoken(arq, tipo, arrToken, scout, linha, coluna):
       token = Token(arq[scout], tipo, linha, coluna, 0, 0)
       arrToken.append(token)

def simplecrawler(arq, sentinela, scout, arrToken, linha, coluna):
   if re.match(operador, arq[scout]):
       faztoken(arq, 'operador', arrToken, scout, linha, coluna)
   elif arq[scout] == ';':
       faztoken(arq, 'pontoevirgula', arrToken, scout, linha, coluna)
   elif arq[scout] == '(':
       faztoken(arq, 'abreparenteses', arrToken, scout, linha, coluna)
   elif arq[scout] == ')':
       faztoken(arq, 'fechaparenteses', arrToken, scout, linha, coluna)
   elif arq[scout] == '[':
       faztoken(arq, 'abrecolchete', arrToken, scout, linha, coluna)
   elif arq[scout] == ']':
       faztoken(arq, 'fechacolchete', arrToken, scout, linha, coluna)
   elif arq[scout] == '{':
       faztoken(arq, 'abrechave', arrToken, scout, linha, coluna)
   elif arq[scout] == '}':
       faztoken(arq, 'fechachave', arrToken, scout, linha, coluna)
   elif arq[scout] == ',':
       faztoken(arq, 'virgula', arrToken, scout, linha, coluna)

