largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 890, 74, 15, 516]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', '\033[1;31m', largest_so_far, '\033[33m')
