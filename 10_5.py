a = (int(input()))
b = []
while a > 0:
  b.append(a % 10)
  a = a // 10
b = b[::-1]
c = 0
for i in b:
    if i%2 == 1:
        c += i**2
print(c)
        
    
