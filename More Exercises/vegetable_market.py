vegetable_kg_price = float(input())
fruits_kg_price = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())
total_bgn = (vegetable_kg_price * total_kg_vegetables + fruits_kg_price * total_kg_fruits) / 1.94
print(format(total_bgn, ".2f"))
