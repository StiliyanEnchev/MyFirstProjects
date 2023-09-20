import math

width_of_ship = float(input())
lenght_of_ship = float(input())
height_of_ship = float(input())
the_average_height_of_astronauts = float(input())

volume_of_rocket = width_of_ship * lenght_of_ship * height_of_ship
volume_of_single_room = (the_average_height_of_astronauts + 0.40) * 2 * 2
number_of_astronauts =  math.floor((volume_of_rocket / volume_of_single_room))

if 3 <= number_of_astronauts <= 10:
    print(f"The spacecraft holds {number_of_astronauts} astronauts.")
elif number_of_astronauts < 3:
    print( "The spacecraft is too small.")
elif number_of_astronauts > 10:
    print("The spacecraft is too big.")