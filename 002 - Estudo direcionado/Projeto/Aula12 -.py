# Efetuando a leitura de um arquivo
#clientes = open("clientes.txt", "r", encoding="utf8")
#clientesModelo = clientes.read()
#print(clientesModelo)

# Efetuando leitura de linha de CSV tabular
#clientes = open("clientes.txt", "r", encoding="utf8")
#clientesModeloLinha = clientes.readline()
#print(clientesModeloLinha)


# Efetuando leitura de CSV usando a biblioteca import CSV
#import csv

#with open("CLIENTES.CSV", "r", encoding="utf8") as myCSVFile:
#    clientes = csv.reader(myCSVFile)

#    for linha in clientes:
#        print(linha)

# Efetuando leitura do item da linha 
#import csv

#with open("CLIENTES.CSV", "r", encoding="utf8") as myCSVFile:
#    clientes = csv.reader(myCSVFile, delimiter=";")

#    for linha in clientes:
#        print(linha)
#        for item in linha:
#            print(item)

# Alterando separador do arquivo para vizualização
import csv

with open("CLIENTES.CSV", "r", encoding="utf8") as myCSVFile:
    clientes = csv.reader(myCSVFile, delimiter=";")

    for linha in clientes:
        print('|'.join(linha))
