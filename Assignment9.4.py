'''text = input("Enter a file name: ")'''
arq = open('mbox-short.txt', 'r')
counts = dict()
#Loop for select lines started with 'From'
for line in arq:
    if line.startswith("From "): #Check if the string start with prefix
        bat = line.split() #Command separat string through of the spaces
        tot = bat[1]
        counts[tot] = counts.get(tot, 0) + 1 # Check if key has in dictionary, if yes return + 1, else return 0
i = None
j = None
# Start count of the words
for k,v in counts.items(): #Loop for key and value together k = key, v = value
    if j is None or j < v:
        j = v
        i = k
        print(i, j)
print(i, j)
