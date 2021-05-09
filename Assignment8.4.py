text = input('Enter a file name: ')
var = open(text, 'r')
lista = list() #Lista vazia criada
for tot in var:
    bat = tot.split()
    for tuf in bat:
        if tuf in lista:
            'done'
        else:
            lista.append(tuf)
lista.sort()
print(lista)

