input_seconds = int(input("Введіть час у секундах: "))
hours = input_seconds // 3600
input_seconds %= 3600
minutes = input_seconds // 60
seconds = input_seconds % 60
midnight_seconds = 24 * 3600
remaining_seconds = midnight_seconds - (hours * 3600 + minutes * 60 + seconds)
print(f"До опівночі залишилось {remaining_seconds // 3600} годин, {remaining_seconds % 3600 // 60} хвилин, {remaining_seconds % 60} секунд.")
