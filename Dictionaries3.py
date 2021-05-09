counts = dict()
names = ['cesv', 'cwen', 'csev', 'zqian', 'cwen', 'name']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)