annual_tax = int(input())
sneakers_price = annual_tax - annual_tax * 0.4
dress_price = sneakers_price - sneakers_price * 0.2
basketball_price = dress_price * 0.25
accessories_price =  basketball_price * 0.2
one_year_price_of_basketball = annual_tax + sneakers_price + dress_price + basketball_price + accessories_price
print(one_year_price_of_basketball)