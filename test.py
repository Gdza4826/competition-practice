word = input()
ls1 = []
ls2 = []
ls3 = []
x = 0
for i in word:
    ls1.append(i)
for i in ls1:
    if i not in ls2:
        ls2.append(i)
    elif ls2[(len(ls2)-1)].isdigit():
        ls2.append(i)
        break
print(ls2)
    