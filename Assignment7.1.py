# Code for open document .txt
text = input('Enter file name: ')
var = open(text, 'r')
for tot in var:
    bat = tot.strip()
    print(bat.upper())

