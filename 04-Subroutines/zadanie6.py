def keyboard():
    for n in range (1,10):
        if(n%3 == 0):
            print(n)
        else:
            print (n, end = " ")
        

keyboard()


def keyboard_alt():
    for x in range(1,8,3):
        print(f"{x} {x+1} {x+2}")

keyboard_alt()