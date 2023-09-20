lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())
fish_tank_volume_in_centimeters = lenght * width * height
fish_tank_volume_in_litres = fish_tank_volume_in_centimeters * 0.001
percent_taken = percent / 100
needed_litters = fish_tank_volume_in_litres * (1 - percent_taken)
print(needed_litters)

