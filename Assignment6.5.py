#encontrando o número
text = "X-DSPAM-Confidence:    0.8475" #String a ser analisada
tot = text.find('0') #Encontrando o primeiro número
num = text[tot:] #atribuindo primeiro número a uma variável e contando a partir dela
print(num) #imprimindo


'''str = "X-DSPAM-Confidence:    0.8475"
ipos  = str.find('0')
piece = str[ipos:]
print(piece)'''



