time_str = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

# Разделяем строку на отдельные временные промежутки по запятой
time_segments = time_str.split(',')

# Проходим циклом по каждому промежутку времени
for segment in time_segments:
    # Разделяем промежуток на отдельные элементы (например, '1h' и '45m') по пробелу
    elements = segment.split(' ')
    
    for item in elements:
        # Проверяем наличие часов
        if 'h' in item:
            hours = int(item.replace('h', ''))
            total_minutes += hours * 60
            
        # Проверяем наличие минут
        elif 'm' in item:
            minutes = int(item.replace('m', ''))
            total_minutes += minutes
            
        # Проверяем наличие секунд
        elif 's' in item:
            seconds = int(item.replace('s', ''))
            total_minutes += seconds // 60

# Выводим итоговый результат на экран
print(total_minutes)