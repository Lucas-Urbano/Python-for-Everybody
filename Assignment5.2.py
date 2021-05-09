largest = -1
smallest = None
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        var = int(num)
        if var > largest:
            largest = var
        if smallest is None:
            smallest = var
        elif var < smallest:
            smallest = var
    except:
        print("Invalid input")
print('Maximum is', largest)
print('Minimum is', smallest)


