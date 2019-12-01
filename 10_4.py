from random import randint
number = randint(1,10)
while True:
    text = (input("Введите число или стоп для выхода: "))
    if text == "выход":
        break
    elif int(text) == number:
        print("Вы угадали")
    elif int(text) > 10:
        print("gwgwegwe")
        break
    elif int(text) > number:
        print("Введеное число больше загаданного")
    elif int(text) < number:
        print("Введеное число меньше загаданного")
    
    
