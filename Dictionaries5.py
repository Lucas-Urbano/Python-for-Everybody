filme = {'Título':'Star Wars', 'ano': '1977', 'diretor': 'George Lucas'}
print(filme.keys())
print(filme.values())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')