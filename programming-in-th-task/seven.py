ls1 = []
ls2 = []
for i in range(9):
    amount = int(input())
    ls1.append(amount)
total = sum(ls1)
debug = total - 100
i = 0
while (i == 0):
    for x in ls1:
        if debug - x in ls1 and x != debug - x:
            ls2.append(x)
            i += 1
for i in ls2:
    ls1.remove(i)
for i in ls1:
    print(i)