## Listas
alunos = []
alunos = ["João Gabriel", "Daniel", "Bruna", "Renata", "Paulo"] 
print(alunos)

#numerosLoteria = []
#numerosLoteria = ["02", "55", "43", "23", "08", "37"]
#print(numerosLoteria)

## Navegando nos itens da lista, atenção o primeiro item é 0
#print(alunos[0])
#print(numerosLoteria[0])
#print(alunos[4])
#print(numerosLoteria[4])

## Um recurso legal é que tambem conseguimos imprimir a lista de trás pra frente
#print(alunos[-1])
#print(numerosLoteria[-1])
#print(alunos[-4])
#print(numerosLoteria[-4])

## Atualizando valores na lista.
#alunos[0] = "Herick"
#print(alunos)

## Remover valores na lista.
#alunos.remove("João Gabriel")
#print(alunos)

## Deletar valores na lista, um item específico.
#del alunos[0]
#print(alunos)

## Efetuar inclusão de aluno
#alunos.append("Herick")
#print(alunos)

## Trabalhanddo com index, o retorno será o primeiro item que encontrart
#alunos = []
#alunos = [ "João Gabriel", "Daniel", "Bruna", "Bruna", "Renata", "Paulo"] 
#print(alunos.index("Bruna"))

## Trabalhanddo com index, pesquisar um indice que não existe
#alunos = []
#alunos = [ "João Gabriel", "Daniel", "Bruna", "Bruna", "Renata", "Paulo"] 
#print(alunos.index("Herick"))
##ValueError: 'Herick' is not in list

## Então se quisermos fazer uma impressão colunar de todos registros da lista podemos efetuar um loop
#for aluno in alunos:
#    print(aluno)   
## Então ao efetuarmos a impressão com for é como fazer print(alunos[N]) N = se refere a cada um dos registros existentes

## Uma outra opção de fazer a contamgem e impressão desta lista é usar len para definir o range de atuação do loop
#for indice in range(len(alunos)):
#    print(alunos[indice])   
#print("Esta listagem possui {} aluno(s)".format(len(alunos)))

## Ou
#qtdAlunos = 0
#qtdAlunos = (len(alunos))
#for indice in range(qtdAlunos):
#    print(alunos[indice])   
#print("Esta lista possui {} aluno(s)".format(qtdAlunos))

## Colocando a lista em ordem alfabética
#alunos.sort()
#print(alunos)
