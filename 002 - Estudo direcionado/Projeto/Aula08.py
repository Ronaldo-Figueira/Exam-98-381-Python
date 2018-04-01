# Usando a biblioteca turtle para desenha um quadrado
#import turtle
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)

# Usando a biblioteca turtle com loop para desenha o mesmo quadrado
#import turtle
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)

# Também podemos colocar um loop dentro de outro loop
#import turtle
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)
#    for steps2 in range(4):
#        turtle.forward(50)
#        turtle.right(90)

# Tambem é possivel usar a biblioteca para realizar desenho mais elaborados
#import turtle
#for steps in range(5):
#    turtle.forward(100)
#    turtle.right(360/5)
#    for steps in range(5):
#        turtle.forward(50)
#        turtle.right(360/5)

## Uma boa prática de programação é passar os parâmetros em variáveis, assim reduzirá a mão de obra numa manutenção futura
#import turtle
#nr_lados = 4
#for steps in range(nr_lados):
#    turtle.forward(100)
#    turtle.right(90)
#    for steps2 in range(nr_lados):
#        turtle.forward(50)
#        turtle.right(90)

## Podemos tambem definir um início e fim para o range de execução.
#for steps in range(1,4):
#    print(steps)

## Podemos tambem definir um salto dentro do início e fim do range. O salto é 3
#for steps in range(1,20,3):
#    print(steps)

## Também há a necessidade de trabalharmos com arrays de variáveis. Salvo que serão sempre strings - Não carrega a informação range
#for steps in [1,2,3,4,5,6,7,8,9,0]:
#    print(steps)

# Vamos representar uma execução de loop com usando a informação do array 
import turtle
for cores in ["blue","red","black","green"]:
    turtle.color(cores)
    turtle.forward(100)
    turtle.right(90)
