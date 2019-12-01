from random import choice
L = ['самовар', 'весна', 'лето']
word = choice(L)
letter = choice(word)
a = input("Угадайте букву: ")
if a == letter:
    print("Вы угадали это буква:", letter)
else:
    print("Вы не угадали, это буква", letter, "из слова", word)

