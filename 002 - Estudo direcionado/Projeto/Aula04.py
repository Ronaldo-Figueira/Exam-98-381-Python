# Manipulação de números
# Calculando area de um triangulo

area = 0

largura = 10
altura = 10

area = (largura * altura) / 2
# impressão decimal
print("A área do tringulo é %d" %area)
# impressão flutuante
print("A área do tringulo é %f" %area)
# impressão flutuante com duas casas decimais
print("A área do tringulo é %.2f" %area)
# impressão preenchendo com zeros a esquerda, muito útil para relatórios.
print("A área do tringulo é %06d" %area)



# Manipulação de números
# Calculando área de um triangulo usando format
area = 0
largura = 10
altura = 10
area = (largura * altura) / 2
# impressão decimal
print("A área do tringulo é {0:d}".format(500))
# impressão flutuante
print("A área do tringulo é {0:f}".format(area))
# impressão flutuante com duas casas decimais
print("A área do tringulo é {0:.2f}".format(area))

# Agora iremos validar a impressão com multiplas variáveis.
print("A primeira variável é {0:d}, a segunda é {1:.3f} e " + 
"a terceira é {2:03d}".format(10,20.999,5))
