name = input('Enter a file name: ')
arq = open(name, 'r')
for line in arq:
    if line.startswith("From "):
        bat = line.split()
        print(bat)
    for tot in bat:
        if tot.startswith(":"):
            tuf = tot.rstrip()
            print(tuf)
