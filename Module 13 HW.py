tickets=int(input("Введите количество билетов: "))
count=0
for i in range(tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        count += 0
    elif ((age >= 18) and (age <= 25)):
        count += 990
    elif age > 25:
        count += 1390

if tickets > 3:
    count = count * 0.9
print("Стоимость заказа:", int(count), "руб.")