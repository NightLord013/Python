s = input("Введите текст: ")
words = s.split()
a = 0
for i in words:
    if len(i) > a:
        a = len(i)
        word = i
if word in words:
    print(words.index(word)+1)

    
    
