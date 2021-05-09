counts = dict()
names = ['yan', 'jjj']
for name in names:
    if name in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
