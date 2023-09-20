group_number = int(input())
musala_climbers = 0
monblan_climbers = 0
kilimandjaro_climbers = 0
ktwo_climbers = 0
everest_climbers = 0
total_climbers = 0
for num_of_group in range(group_number):
    number_of_people = int(input())
    total_climbers += number_of_people
    if number_of_people <= 5:
        musala_climbers += number_of_people
    elif number_of_people <= 12:
        monblan_climbers += number_of_people
    elif number_of_people <= 25:
        kilimandjaro_climbers += number_of_people
    elif number_of_people <= 40:
        ktwo_climbers += number_of_people
    elif number_of_people >= 41:
        everest_climbers += number_of_people
percentage_musala_climbers = musala_climbers / total_climbers * 100
percentage_monblan_climbers = monblan_climbers / total_climbers * 100
percentage_kilimandjaro_climbers = kilimandjaro_climbers / total_climbers * 100
percentage_ktwo_climbers = ktwo_climbers / total_climbers * 100
percentage_everest_climbers = everest_climbers / total_climbers * 100
print(f"{percentage_musala_climbers:.2f}%")
print(f"{percentage_monblan_climbers:.2f}%")
print(f"{percentage_kilimandjaro_climbers:.2f}%")
print(f"{percentage_ktwo_climbers:.2f}%")
print(f"{percentage_everest_climbers:.2f}%")