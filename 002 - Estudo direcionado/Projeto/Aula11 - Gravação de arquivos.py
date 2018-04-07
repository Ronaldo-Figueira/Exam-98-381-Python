############## WRITE

# Efetuando a leitura de um arquivo, mesmo se tratando de um gravação o comando continua sendo open. 
# Usando w - Caso o arquivo não exista ele será criado na execução, se existir o mesmo será substituído
# Usando a - Caso o arquivo não exista ele será criado na execução, se existir o os dados gerados serão incluídos.
# Caso ocorra a necessidade de efetuar a leitura e gravação no mesmo código use w+
demo = open("demo.txt","w")
demo.write("Criando primeira linha \n")
demo.write("Criando segunda linha \n")
demo.write("Criando terceira linha \n")
demo.write("Welcome!!")
## Atenção é indispensável o uso do close, senão o arquivo poderá abresentar dado sujo ou inválido... por estar em uso.
demo.close()


#print("A gravação ocorreu com sucesso")

# Efetuando uma interação para gravar em arquivo
dados = input("Informe os nomes dos convidados: ")

arquivo = open("demo.csv","w")
arquivo.write(dados)
arquivo.close()

print("Dados gravados com sucesso! ")

