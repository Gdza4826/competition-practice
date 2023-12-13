mn = input()
k = int(input())
kk = k
test_list = []

list01 = []
list03 = []
list01 = mn.split(" ")

for i in range(int(list01[0])):
    test_list.append([])
for i in test_list:
    for j in range(int(list01[1])):
        i.append("_")

for j in range(len(list01)):
    list01[j] = int(list01[j])

for i in range(k):
    rc = input()
    list02 = []
    list02 = rc.split(" ")
    for k in range(len(list02)):
        list02[k] = int(list02[k])
    list03.append(list02)

for l in range(kk):
    test_list[(list03[l][0])-1][(list03[l][1])-1] = "X"

xyz = 0

for i in test_list:
    for j in i:
        xyz = xyz + 1
        print(j,end='')
        if xyz == int(list01[1]):
            xyz = 0
            print("")
    



