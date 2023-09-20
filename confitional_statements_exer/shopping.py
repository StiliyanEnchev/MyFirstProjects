petars_budget = float(input())
purchased_video_cards = int(input())
purchased_processors = int(input())
purchased_ram_memory = int(input())
video_card_price = 250
total_of_video_cards = purchased_video_cards * video_card_price
price_for_processor = total_of_video_cards * 0.35
price_for_ram_memrory = total_of_video_cards * 0.10
total_of_processors = purchased_processors * price_for_processor
total_of_ram_memory = purchased_ram_memory * price_for_ram_memrory
total_sum = total_of_processors + total_of_video_cards + total_of_ram_memory
if purchased_video_cards > purchased_processors:
    total_sum = total_sum * 0.85
if petars_budget >= total_sum:
    print(f"You have {petars_budget - total_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_sum - petars_budget:.2f} leva more!")