#EXERCICIO 05
import random

matriz = [[random.randint(-100, 100) for _ in range(5)] for _ in range(5)] #"random.randint" gera um numero inteiro entre -100 e 100 "for _ in range" foi utilizado para incluir 5linhas e 5colunas

print("Matriz 5x5:")
for linha in matriz:
    print(linha)
maior = matriz[0][0] 

for linha in matriz:
    for elemento in linha: #O if verifica se o "elemento" atual é maior do que o que está salvo em "maior". Se for, ele atualiza a variável maior

        if elemento > maior:
            maior = elemento

print(f"\nO maior elemento da matriz é: {maior}") #Imprime o numero encontrado