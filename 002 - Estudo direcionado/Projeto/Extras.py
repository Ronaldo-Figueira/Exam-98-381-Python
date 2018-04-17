
# Avançando no estudo direcionado, aulas extras Gustavo Guanabara.

# Tipos primitivos ou tipo de variáveis
    #   int     = [7, -4, 0, 9875 ] 
    #   float   = [4.5, 0.076, -15.223, 7.0] 
    #   bool    = [ True, False]
    #   str     = ['Olá', 'Seja bem vindo', '20', '7.0','']  

## Toda entrada de dados é str, por este motivo usamos int() para conversão. 
#n1 = int(input('Informe o primeiro número: '))
#n2 = int(input('Informe o segundo número: '))
#soma = n1+n2
#print('A soma entre {} e {} vale {} .'.format(n1, n2, soma))

## Identificando tipo de variáveis.
#n1 = input('Informe algo: ')
#print('O tipo do dado informado é {} .' .format(type(n1)))
#print('O dado é numerico? {} .'.format(n1.isnumeric()))
#print('O dado é alfanumerico? {} .'.format(n1.isalnum()))
#print('O dado é alfa? {} .'.format(n1.isalpha()))
#print('O daos esta em caixa alta? {} .'.format(n1.isupper()))
#print('O daos esta em caixa baixa? {} .'.format(n1.islower()))

## Operações aritiméticas.
#    # + Adição, - Subtração, * Multiplicação, / Divisão, ** Potência, // Divisão inteira, % Módulo ou Resto
#    # Quando quiser testar se algo é igual a outro use ==
#n1 = int(input('Informe o primeiro número: '))
#n2 = int(input('Informe o segundo número: '))
#print('O módulo ou resto da divisão é {} .'.format(n1 % n2))
    
#    # Ordem de procedência para execução dos operadores.
#    # 1º (), 2º **, 3º * / // %, 4º + -
#print(10*3+5**2) #55
#print(80-70+5//2+5%2) #13
#print(81**(1/2)) #9 Raiz quadrada é o numero dividido por 0.5
#print(127**(1/3)) # Raiz cúbica
#print('=' * 50) # relacionamento entre operadores e strings

## Loops e tomadas de decisão.
#    # Seleção unica
#nome = input('Informe seu nome: ')
#if nome.isupper() :
#    print('Nome escrito em caixa alta! ')

#    # Seleção Dupla opção 1
#nome = input('Informe seu nome: ')
#if nome.isupper() :
#    print('Nome escrito em caixa alta! ')
#else :
#    print('Nome escrito em caixa baixa! ')

#    # Seleção Dupla opção 2 
#nome = input('Informe seu nome: ')
#if nome.isupper() :
#    print('Nome escrito em caixa alta! ')
#elif nome.islower() : # elif pode ser usado quantas vezes forem necessárias.
#    print('Nome escrito em caixa baixa! ')

#    # Outra opção
#resposta = input('Informe Sim ou Não: ')
#if resposta.upper() == 'SIM':
#    print('Você respondeu Sim!')
#elif resposta.upper() == 'NÃO' or resposta.upper() == 'NAO':
#    print('Você respondeu Não!')
#else:
#    print('Resposta errada! ')


## Definindo e executando uma função com variável
#def soma(numero1, numero2):
#    resultado=numero1+numero2
#    return resultado

#retorno = soma(12.25, 75.6)
#print(retorno)

## Definindo e executando uma função sem variável
#def imprime():
#    print('Oi!!')
#    return

#imprime()

## Definindo e executnado função associada a if, else com retorno True ou False
#def temSeteLetras(palavra):
#    if len(palavra) == 7:
#        return "Tem sete letras"
#    elif len(palavra) != 7:
#        return "Não tem sete letras"
#palavra=''
#palavra=input('Informe uma palavra: ')
#print(temSeteLetras(palavra))

# Entrada e arquivos de arquivos.
# Alguns dos métodos do objeto:
#  read() – lê todo o conteúdo do arquivo
#  readline() – lê uma linha do arquivo
#  readlines() – lê todas as linhas do arquivo
#  seek() – posiciona o “cursor” de leitura
#  write(conteudo) – escreve ‘conteudo’ no arquivo

#listaClientes = ''
#clientes = ''
#clientes = open('CLIENTES.CSV','r',encoding='utf-8')
#listaClientes = clientes.read()
#print(listaClientes)
#clientes.close()

## Escrevendo lista de nomes
#nome = ''
#listaNomes =''

#file = open('FAMILIA.TXT', 'a', encoding='utf-8')
#while nome.upper() != 'NONE' :
#    nome = input('Informe o nome: ' )
#    if nome.upper() != 'NONE' :
#        file.write(nome.upper() + '\n')
#    else: 
#        continue

#file.close()

## Pesquisando na lista de nomes
#file = open('FAMILIA.TXT','r', encoding='utf-8')
#nomes = file.read()
#if 'HERICK' in nomes:
#    print('Nome encontrado')


# Remover na lista de nomes
file = open('FAMILIA.TXT','r', encoding='utf-8')
nomes = file.read()
if 'HERICK' in nomes:
    nomes.remove('HERICK')
    print('Nome removido! ')