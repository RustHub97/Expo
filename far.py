money = float(input("Введите сумму вклада: "))
time = int(0)
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

print("Годовой доход: ")

bank1 = round(per_cent.get('ТКБ') / 100 * money)
print("ТКБ: ", bank1, "руб")
bank2 = round(per_cent.get('СКБ') / 100 * money)
print("СКБ: ", bank2, "руб")
bank3 = round(per_cent.get('ВТБ') / 100 * money)
print("ВТБ: ", bank3, "руб")
bank4 = round(per_cent.get('СБЕР') / 100 * money)
print("СБЕР: ", bank4, "руб")

deposit=[]
deposit.append(bank1)
deposit.append(bank2)
deposit.append(bank3)
deposit.append(bank4)
print(deposit)

maxi = round(max(deposit))
bank = max(per_cent, key=per_cent.get)

print("Максимальная сумма, которую вы можете заработать: ", maxi, "руб")
print("Банк, обеспечивающий максимальный доход: ", bank)