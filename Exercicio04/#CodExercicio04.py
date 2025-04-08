#EXERCICIO 04
import random #Novamente importei essa biblioteca para permitir que eu gere numeros aleatorios

# Criando a matriz 3x3 com números reais positivos entre 1.0 e 100.0
matriz = [[round(random.uniform(1.0, 100.0), 2) for _ in range(3)] for _ in range(3)] #"random.uniform(1.0, 100.0)" gera um número real aleatório entre 1.0 e 100.0. --- "round(..., 2)" arredonda o número para duas casas decimais.

print("Matriz 3x3:") # Exibindo a matriz
for linha in matriz:
    print(linha)

print("\nSoma dos elementos de cada linha:")
for i, linha in enumerate(matriz):
    soma = sum(linha) #Calcula a soma dos 3 valores daquela linha usando "sum()"
    print(f"Linha {i + 1}: soma = {soma:.2f}")
