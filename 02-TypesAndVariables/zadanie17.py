height_cm = int(input("podaj wzrost: "))
height_in = int(height_cm/2.54)
height_feet = int(height_in/12)

print("I am {}cm tall, i.e. {} feet and {} inches.".format(height_cm, height_feet, height_in%12))