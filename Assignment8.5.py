text = input('Enter a file name: ')
arq = open(text, 'r')
count = 0
for line in arq:
    line = line.rstrip() # Remove espaços antes e depois da linha
    if not line.startswith('From '): # Busca linhas iniciadas com From
        continue #Daqui volta para o for, até terminar as linhas do arquivo
    count = count + 1 # Conta a quantidade de linhas iniciadas com From
    bat = line.split() #Separa as linhas em strings pelos espaços das palavras
    print(bat[1]) # 0 é o From, 1 começa o endereço de email desejado
print("There were", count, "lines in the file with Form as the first word")