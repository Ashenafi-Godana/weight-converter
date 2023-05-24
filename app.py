weight = float(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit == 'l' or unit == 'L':
    result = 0.45 * weight
    print(f'You are {result} kilos')
elif unit == 'k' or unit == 'K':
    result = weight / 0.45
    print(f'You are {result} pounds')