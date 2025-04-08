#EXERCICIO 03
import random #Importei essa biblioteca para permitir que eu gere 10 numeros aleatorios entre 1 a 100
vetor = [random.randint(1, 100) for _ in range(10)] #"random.randint" foi utilizado para gerar os numeros aleatorios --- "for _ in range(10)" repete o processo 10 vezes

print("Vetor:", vetor)

valor = int(input("Digite um valor inteiro e positivo para procurar no vetor: ")) #Exibe uma mensagem para que o usuario possa escrever o numero escolhido

if valor in vetor: #Verifica se o valor digitado existe dentro do vetor
    indice = vetor.index(valor)
    print(f"O valor {valor} foi encontrado no índice {indice}.") #Informa ao usuario em qual posição o valor foi encontrado
else:
    print(f"O valor {valor} não existe no vetor.") #Caso o valor não tenha sido encontrado, informa ao usuario que o valor não foi encontrado
