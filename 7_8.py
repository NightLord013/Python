from random import randint
a = randint(1,6)
b = randint(1,6)
print("Первый игрок: ", a, "Второй игрок: ", b , end= "\n" )
if a > b:
    print("Первый игрок победил")
elif a < b:
    print("Второй игрок победил")
else:
    print("Ничья")
