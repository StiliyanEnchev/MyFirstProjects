pack_pens = 5.80
pack_markers = 7.20
litters_detergent = 1.20
pens = int(input())
markers = int(input())
detergent = int(input())
discount = int(input())
total_without_discount = pens * pack_pens + markers * pack_markers + detergent * litters_detergent
total_sum_with_discount = total_without_discount - (total_without_discount * discount / 100)
print(total_sum_with_discount)
