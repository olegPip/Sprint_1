worid_champions = {
    2002: "Бразилия",
    2006: "Италия",
    2010: "Испания",
    2014: "Германия",
    2018: "Франция"
}

# Добавили 2022 Аргентину в словарь
worid_champions[2022] = "Аргентина"

# Вывели всех чемпионов в формате год-страна
for year, champiom in worid_champions.items():
    print(f"{year} - {champiom}")

country = "Италия"

# Проверяем, наличие в словаре страны
if country in worid_champions.values():
    print(f"{country} становилась чемпионом мира по футболу в 21 веке!")
else:
    print(f"{country} не выигрывала чемпионат мира по футболу в 21 веке.") 