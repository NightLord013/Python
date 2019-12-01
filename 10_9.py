s = input()
total = 0
q = 0
z = 0
for i in range(len(s)):
    if s[i].isalpha():
        continue
    elif s[i] == ' ':
        continue
    total=total+int(s[i])
    q += 1
    if int(s[i]) > z:
        z = int(s[i])
print("сумма чисел:", total)
print("количество цифр:", q)
print("максимальное: ", z)
