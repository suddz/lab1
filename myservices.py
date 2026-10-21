services = [
    {
        "name": "Чистка пальто",
        "type": "Верхняя одежда",
        "branches": ["Центр", "Север", "Юг"],
        "prices": [1500, 1400, 1600]
    },
    {
        "name": "Чистка костюма",
        "type": "Деловая одежда",
        "branches": ["Центр", "Север", "Юг"],
        "prices": [1200, 1100, 1250]
    },
    {
        "name": "Выведение пятен",
        "type": "Спецобработка",
        "branches": ["Центр", "Север", "Юг"],
        "prices": [600, 550, 700]
    },
    {
        "name": "Чистка пуховика",
        "type": "Верхняя одежда",
        "branches": ["Центр", "Север", "Юг"],
        "prices": [1800, 1700, 1900]
    },
    {
        "name": "Чистка свадебного платья",
        "type": "Деликатные ткани",
        "branches": ["Центр", "Юг"],
        "prices": [3500, 3800]
    },
    {
        "name": "Чистка ковра",
        "type": "Домашний текстиль",
        "branches": ["Север", "Юг"],
        "prices": [850, 950]
    }
]


def print_services(items):
    print(u"Услуга".ljust(26), u"Тип".ljust(20),
          u"Филиалы".ljust(28), u"Стоимость, руб.".ljust(20))
    for item in items:
        print(item["name"].ljust(26), item["type"].ljust(20),
              str(item["branches"]).ljust(28), str(item["prices"]).ljust(20))


def average(values):
    """Среднее арифметическое списка чисел."""
    return sum(values) / len(values)


def filter_by_average(items, min_average):
    """Возвращает услуги, средняя стоимость которых по филиалам выше заданной."""
    return [item for item in items if average(item["prices"]) > min_average]


print("Все услуги:")
print_services(services)
print()
try:
    threshold = float(input("Введите минимальную среднюю стоимость услуги: "))
except ValueError:
    print("Ошибка: необходимо ввести число.")
else:
    print("Услуги со средней стоимостью выше", str(threshold) + ":")
    print_services(filter_by_average(services, threshold))
