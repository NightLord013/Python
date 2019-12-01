from random import randint
a = (int(input()))
b = (int(input()))
c = [[randint(0,9) for i in range (a)] for i in range(b)]
for i in c:
    print()
    for j in i:
        print(j, end = "")
