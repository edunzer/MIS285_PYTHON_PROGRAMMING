## WEIGHT LOSS

w_start = int(input("Please enter in your start weight: "))

def chart(w_start):
    print('Month\t   Weight')
    print('----------------')

    for m in range (0, 7, +1):
        w = (w_start-(4*m))
        print(m, '\t', w)

chart(w_start)
