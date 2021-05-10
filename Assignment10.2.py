name = input('Enter a file name: ')
arq = open(name)
hrcount = dict() #Dictionary empty
hlist = list() #List empty
for line in arq: #Loop for filter words
    if line.startswith("From "): #Select line started with From
        bat = line.split() #Slice line
        hr = bat[5].split(':') ##Select starting of the 5 and slice from ':'
        hrcount[hr[0]] = hrcount.get(hr[0], 0) + 1 #Checking if each word is on the dictionary
for k, v in hrcount.items(): #Loop for counting key and value
    tuf = (k, v) # add key e value on the tuf variable
    hlist.append(tuf) #add tuf variable on the hlist, through append
hlist = sorted(hlist, reverse=True) #Sort hlist
for k, v in hlist[:]:#Loop for print key and value off the list
    print(k, v)
