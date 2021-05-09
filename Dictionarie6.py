Movie1 = {'Título':'Star Wars', 'ano': '1977', 'diretor': 'George Lucas'}
Movie2 = {'Título':'Indiana Jones e os salteadores da arca perdida', 'ano': '1981', 'diretor': 'Steven Spielberg'}
Movie3 = {'Título':'Matrix', 'ano': '1999', 'diretor': 'Irmãos Wachowski'}
Movie1['País'] = 'EUA' #add keys e value in a dictionary Movie1
print()
print()
print(Movie3.keys())
print()
print(Movie3.values())
print()
print(Movie3.items())
print()
print()
print(Movie1)
print('ano' in Movie1) #checking key in a dictionary
print('Velozes e Furiosos' in Movie2) #checking key in a dictionary Movie2, this search a keys
print('diretor' in Movie2) #checking key
print(Movie1.get('País', 'Informação não disponível'))
print(Movie1.get('diretor', 'Informação não disponível'))
print('Done')