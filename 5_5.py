cod = (int(input("Введите код города: ")))
d = (int(input("Длительность преговоров: ")))
if cod == 343:
    summa = 15
elif cod == 381:
    summa = 18
elif cod == 473:
    summa = 13
elif cod == 485:
    summa = 11
else:
    print("Нет такого кода!")
print("Стоимость переговоров:  ",summa * d)
