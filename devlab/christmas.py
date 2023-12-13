num = int(input())
list01 = []
num2 = (num*2)+1
for i in range((num2-num)):
    list01.append(((' '*i)+((num2-(i*2))*"*")))
list01.reverse()
for j in range(num):
    for k in range((j+2)):
        print(list01[k])
print((" "*num)+"|")
print(("="*num)+"V"+("="*num))
