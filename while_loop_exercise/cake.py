width = int(input())
length = int(input())
total_pieces = width * length
cake_is_over = False
action = input()
while action != "STOP":
    taken_pieces = int(action)
    total_pieces -= taken_pieces
    if total_pieces < 0:
        cake_is_over = True
        break
    action = input()
if cake_is_over:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
else:
    print(f"{total_pieces} pieces are left.")