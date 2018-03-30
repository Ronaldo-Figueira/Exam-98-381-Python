# Agora iremos representar operações matemáticas.
# É muito importante classificar suas variáveis durante o processo de calculo.

salario = input("Informe seu salário " )
comissao = input("Informe sua comissão ")
cheque = salario + comissao

print("Voce irá receber {0}".format(cheque))


chequeFinal = int(salario) + int(comissao)


print("Voce irá receber {0}".format(chequeFinal))


# Reescrevendo o código usando boas práticas.
salarioInt = float(input("Informe seu salário " ))
comissaoInt = float(input("Informe sua comissão "))
chequeInt = salarioInt + comissaoInt

print("Voce irá receber {0:.2f}".format(chequeInt))
