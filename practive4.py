file_size_gb = float(input("Введіть розмір файлу в гігабайтах: "))
internet_speed_bps = float(input("Введіть швидкість інтернет-з'єднання в бітах на секунду: "))
file_size_bytes = file_size_gb * 1024 * 1024 * 1024
download_time_seconds = file_size_bytes / internet_speed_bps
download_time_hours = int(download_time_seconds // 3600)
download_time_seconds %= 3600
download_time_minutes = int(download_time_seconds // 60)
download_time_seconds %= 60
print(f"Час завантаження: {download_time_hours} годин, {download_time_minutes} хвилин, {int(download_time_seconds)} секунд")
