word = input()

list01 = []
list02 = []
list03 = []
x = 0

for l in word:
    list02.append(l)

for i in range(len(list02)):
    # print(i)
    for j in list02:
        list01.append(j)
    for k in range(len(list01)):
        x = x + 1
        list01.pop()
        list01.pop(0)
        # print(list01)
        if len(list01) == 1 + (i * 2) or len(list01) == 2 + (i * 2):
            print(" "*x,end="")
            for li in list01:
                print(li,end="")
            print(" "*x)
        if len(list01) == 0 or len(list01) == 1:
            break
    x = 0
    list01.clear()
print(word)
for p in word:
    list03.append(p)
for q in range(len(list03)):
    list03.pop()
    list03.pop(0)
    if len(list03) == 0:
        break
    print(" "*(q + 1),end="")
    for il in list03:
        print(il,end="")
    print(" "*(q + 1))
    if len(list03) == 0 or len(list03) == 1:
        break
    