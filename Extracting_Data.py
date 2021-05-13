import re
x = input('Enter a file: ')
y = open(x, 'r')
lista = list()
for z in y: #
    z = z.rstrip()
    for w in z:
        w = re.findall('[0-9]+',z)
        if not w in lista:
            lista.append(w)
soma = []
for i in lista:
    soma = soma + i
valores = []
count = 0
for val in soma:
    count = count + 1
    valores.append(int(val))
print("There are {} values and the sum is {}". format(count, sum(valores)))

