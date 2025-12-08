def even_odd(start, end):
    for num in range(start, end + 1):
        if num%2==0:
            print(f'{num} is even')
        else:
            print(f'{num} is odd')

even_odd(100, 500)