one_bitcoin_in_leva = 1168
one_chinesse_iun_in_dollars = 0.15
one_dollar_in_leva = 1.76
one_euro_in_leva = 1.95
total_bitcoins = int(input())
total_chinesse_iuns = float(input())
comision = float(input())
total_in_leva = total_bitcoins * one_bitcoin_in_leva
total_in_dollars = total_chinesse_iuns * one_chinesse_iun_in_dollars
total_in_leva = total_in_leva + total_in_dollars * one_dollar_in_leva
total_in_euro = (total_in_leva / one_euro_in_leva)
total_with_comision = total_in_euro - (total_in_euro * comision / 100)
print(f"{total_with_comision:.2f}")