word = input()
ls = []
for i in word:
    if i.isdigit():
        ls.append(i)
print(ls)