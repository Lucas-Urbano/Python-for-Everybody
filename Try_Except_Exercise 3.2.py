hours = input('Enter hours: ')
rate = input('Enter a rate: ')
try:
    h = float(hours)
    r = float(rate)
except:
    print('Please enter numeric input')
    quit()

pay = h * r
print(pay)
