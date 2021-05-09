#Programa que seleciona e imprime o maior e menor número da lista (Exercício 6 do capítulo 8)
numlist = list() #Lista vazia criada
while True:
    num = input('Enter a number: ')
    if num == 'done': #Comando para encerrar o programa
        break
    value = float(num) #Transforma a string em float
    numlist.append(value) #Insere o número digitado na lista
print('Maximum:', max(numlist))
print('Minimum:', min(numlist))