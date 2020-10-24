## CELSIUS TO FAHRENHEIT TABLE

def conversion():

    print('Celsius\t   Farenheit')
    print('---------------------')

    for c in range (0, 21, +1):
        f = (9 / 5) * c + 32
        print(c, '\t', format(f, '.1f'))

conversion()
