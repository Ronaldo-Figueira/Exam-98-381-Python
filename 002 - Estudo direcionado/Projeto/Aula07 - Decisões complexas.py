## Decisões complexas. 
## Vamos abordar um exemplo de possibilidades de respostas dependendo do idioma de entrada.

#idioma = input("Qual idioma o Sr(a) fala? ").upper()
#if idioma == "PORTUGUES":
#    print("Bom dia ")

#elif idioma == "INGLES":
#    print("Good Morning")

#elif idioma == "ESPANHOL":
#    print("Buenos dias")

# Validando and e or na mesma instrução, para isso iremos representar um processo de brindes de cartão de credito
# Se o cartão for outro ou prata e o consumo superior a valor X, o titular do cartão ganhará um brinde.
tipoCartao = input("Informe o tipo do cartão: ").upper()
fatura = 1300.00

if fatura >= 1100.00 and (tipoCartao == "OURO" or tipoCartao == "PRATA"):
    print("Parabêns! Você ganhou um brinde")
print("Tenha um bom dia!")


alunos = []
alunos = ["João Gabriel", "Daniel", "Bruna", "Renata", "Paulo"] 
print(alunos)

nome = input('Informe o nome do aluno(a): ')
if nome in alunos:
    print('Aluno(a) encontrado(a) no indice {}.'.format(alunos.index(nome)))
else:
    print('Aluno não encontrado. ')