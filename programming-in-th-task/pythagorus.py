import math
number = input()
ls = []
ls.append(number)
ls2 = []
ls3 = []

for i in ls:
    ls2 = i.split()
for i in ls2:
    counter = float(i)
    ls3.append(counter)
total = math.sqrt((ls3[0]*ls3[0]) + (ls3[1]*ls3[1]))

print("{0:.6f}".format(total))