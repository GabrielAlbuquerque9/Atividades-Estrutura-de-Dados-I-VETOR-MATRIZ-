#EXERCICIO 02
matriz = [] #Criei uma uma lista chamada matriz
letra = 'a' #Aqui eu comecei com a letra "a" pois ela sera a primeira letra em nossa matriz
for i in range(4): #Um laço que executará as 4 linhas da matriz
    linha = [] #Lista vazia chamada "linha" para armazenar os dados da matriz
    for j in range(4): #Criei uma sequencia de numeros, partindo do 0 (0, 1, 2, 3)
        linha.append(letra) #Adiciona a letra atual à linha
        letra = chr(ord(letra) + 1)  #chr=transforma de volta em letra, só que a próxima --- ord=pega o código numérico da letra utilizando o ASCII
    matriz.append(linha) #Depois de montar a linha completa com 4 letras, ela é adicionada à matriz
for linha in matriz:
    print(" ".join(linha))
