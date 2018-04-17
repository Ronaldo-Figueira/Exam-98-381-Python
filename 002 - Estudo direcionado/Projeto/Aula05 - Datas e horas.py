# Aula 05 - Trabalhando com datas
#import datetime
#dataAtual = datetime.date.today()
#print(dataAtual)
#print(dataAtual.year)
#print(dataAtual.month)
#print(dataAtual.day)
#print(dataAtual.strftime("%d %b, %Y"))

# Efetuando input de datas
#import datetime
#currentDate = datetime.datetime.now()
#aniversario = input("Informe sua data de aniversário DD/MM/YYYY: ")
#dataAniversario = datetime.datetime.strptime(aniversario,"%m/%d/%Y").date()
#print(dataAniversario)
#days = (dataAniversario - currentDate)
#print(days.days)

# Trabalhando com tempo
#import datetime
#currentTime = datetime.datetime.now()
#print(currentTime)
#print(currentTime.hour)
#print(currentTime.minute)
#print(currentTime.second)

#import datetime
#currentTime = datetime.datetime.now()
#print(currentTime.time())
#currentDate = datetime.date.today()
#print(currentDate)

## Calculando idade
#import datetime
#data = input("Informe sua data de nascimento no formato DD/MM/YYYY: ")
#dataNascimento = datetime.datetime.strptime(data,'%d/%m/%Y').date()
#idade = (datetime.date.today() - dataNascimento)
#print("Sua idade é {}".format(int(idade.days/365)))

# Data Atual
import datetime

currentDate = datetime.date.today()
print(currentDate)