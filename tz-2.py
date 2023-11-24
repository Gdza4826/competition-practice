thon = int(input())
raca = int(input())

list01 = []
list02 = []
x = 0
y = 0
for i in range(thon):
    racathon = int(input())
    list01.append(racathon)

print(list01)

for j in list01:
    x = x + j
    list02.append(x)

# print(list02)

list02.reverse()

print(list02)

for l in range(len(list02)):
    if list02[l] > raca:
        y = y + 1
if y == len(list02):
    print("0")
else:
    pass

for k in range(len(list02)):
    if list02[k] <= raca:
        print(len(list02) - (k))
        break


