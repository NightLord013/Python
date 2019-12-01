s = "Мой дядя самых честных правил, Когда не в шутку занемог, Он уважать себя заставил И лучше выдумать не мог"
words = s.split()
c = []
for i in words:
    if not i.startswith("м") and not i.startswith("М"):
        c.append(i)  
print(" ".join(c))
    
