mackerel_price = float(input())
sprattus_price = float(input())
bonito_in_kg = float(input())
carangidae_in_kg = float(input())
mussel_in_kg = int(input())
bonito_price = mackerel_price + mackerel_price * 0.6
carangidae_price = sprattus_price + sprattus_price * 0.8
mussel_price = 7.50
total_price = mussel_in_kg * mussel_price + carangidae_in_kg * carangidae_price + bonito_in_kg * bonito_price
print(format((total_price), ".2f"))