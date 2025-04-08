#EXERCICIO 01
vetor = [] #Aqui criei uma lista vazia

for i in range(10): #Aqui eu chamei os numeros de 0 a 9 (totalizando 10 valores)
    vetor.append((i + 1) * 10) # "i" assume os valores de 0 a 9, assim somando e logo apos multiplicando assim ficando 10, 20, 30, 40...

print("Valores do vetor:") #Exibe os valores
for valor in vetor:
    print(valor, end=' ') #Mostra tudo na mesma linha e separado por espaços
