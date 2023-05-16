#Titulo: titulo do game (Tam: 50 caracteres)
#Produtora: quem desenvolveu o game (Tam: 40 caracteres)
#Gênero: qual o gênero do game (Tam: 25 caracteres)
#Plataforma: para qual tipo de maquina foi desenvolvido (PC, PS4, Xbox, etc…). Se for para varios, colocar: Multiplataforma (Tam: 15 caracteres)
#Ano: data de release do game (Tam: 4 caracteres)
#Classificacao: classificacao etaria do game (Tam: 12 caracteres)
#Preco: media de preco para o produto (Tam: 7 caracteres)
#Midia: se esta disponivel em formato fisico, digital, ou em ambos (Tam: 8 caracteres)
#Tamanho: tamanho da midia (em GB) (Tam: 7 caracteres)

import math
import sys

file = open(sys.argv[1],"r")
lines = file.readlines()
file.close()

def addNullChar(s, n):
    var = "                                                  "#
    sLen = len(s)
    return s + var[sLen:n]

def addSizeIndicator(s):
    l = len(s)
    return str(l) + s

def writeFixedSize(s, v):
    file = open(s, "a")
    file.write(addNullChar(v[0], 50))
    file.write(addNullChar(v[1], 40))
    file.write(addNullChar(v[2], 25))
    file.write(addNullChar(v[3], 15))
    file.write(addNullChar(v[4], 4))
    file.write(addNullChar(v[5], 12))
    file.write(addNullChar(v[6], 7))
    file.write(addNullChar(v[7], 8))
    file.write(addNullChar(v[8][:len(v[8])-1], 7))
    file.close()

def writeSizeIndicator(s1, s2):
    file = open(s1, "a")
    file.write(addSizeIndicator(s2))
    file.close()

def writeFixedFields(s1, s2):
    file = open(s1, "a")
    file.write(s2)
    file.write("|")
    file.close()

def writeSeparator(s1, s2):
    file = open(s1, "a")
    file.write(s2)
    file.write("#")
    file.close()

#for i in range(len(lines)):
#    splited = lines[i].split("|")
#    writeFixedSize("tamanhoFixo.txt", splited)
#    writeFixedFields("quantidadeDeCampos.txt", lines[i][:len(lines[i])-1])
#    writeSizeIndicator("indicadorDeTamanho.txt", lines[i][:len(lines[i])-1])
#    writeSeparator("delimitador.txt", lines[i][:len(lines[i])-1])

def readFixedSize(s):
    file = open(s, "r")
    file.seek(0, 2)
    fileSize = file.tell()
    file.seek(0, 0)
    buf = []
    while file.tell() < fileSize:
        buf.append(file.read(168))
    return buf

def readSeparator(s):
    file = open(s, "r")
    buf = file.read()
    file.close()
    return buf.split("#")

#def readFixedFields(s):
#    file = open(s, "r")
#    buf = file.read()
#    file.close()
#    fields = buf.split("#")
#    for i in range(len(fields))
#        for j in range(9):
#            record = fields[j] + "|"
    
list = readSeparator("delimitador.txt")
for i in range(len(list)):
    print(list[i])

list = readFixedSize("tamanhoFixo.txt")
for i in range(len(list)):
    print(list[i])

