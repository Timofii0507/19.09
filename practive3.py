price_per_console = float(input("Введіть вартість однієї ігрової приставки: "))
quantity = int(input("Введіть кількість ігрових приставок: "))
discount_percentage = float(input("Введіть відсоток знижки: "))
choice = input("Виберіть 'загальна' або 'поодиноко': ")
if choice == 'загальна':
    total_price = price_per_console * quantity * (1 - discount_percentage / 100)
    print(f"Загальна сума замовлення: {total_price} грн")
elif choice == 'поодиноко':
    individual_price = price_per_console
