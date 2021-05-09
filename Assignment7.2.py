# Programa que abre arquivo .txt seleciona linha específica, seleciona números floats, soma eles, calcula a média e imprime a média.

#Use the file name mbox-short.txt as the file name
file = input('Enter a file name: ')
arq = open(file, 'r')
soma = 0
count = 0
for line in arq:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        tot = line.find('0')
        bat = float(line[tot:])
        print(soma)
        soma = bat + soma
print('Average spam confidence:', soma/count)
