price_for_printing_one_page = float(input())
price_for_printing_one_cover = float(input())
percentage_discount_for_paper = int(input())
sum_for_designer = float(input())
percentage_from_total_sum_by_team = int(input())

total_sum_per_copy = price_for_printing_one_page * 899 + price_for_printing_one_cover * 2
total_sum_per_copy = total_sum_per_copy - (total_sum_per_copy * percentage_discount_for_paper / 100)
total_sum_per_copy += sum_for_designer
total_sum_per_copy = total_sum_per_copy - (total_sum_per_copy * percentage_from_total_sum_by_team / 100)

print(f'Avtonom should pay {total_sum_per_copy:.2f} BGN.')