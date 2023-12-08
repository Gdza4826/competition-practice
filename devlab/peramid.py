# ls_alpha = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ls_num = ["0","1","2","3","4","5","6","7","8","9"]
word = input()
ls1 = []
ls2 = []
ls3 = []
ls4 = [] 
x = 0

for i in word:
    ls1.append(i)

for j in range(len(ls1)):
    if x == 2:
        for k in range(j):
            ls1.pop(0)
        ls3.append(ls2)
        ls2.clear()
    else:
        pass
    if ls1[j] in ls_num:
        ls2.append(ls1[j])
    else:
        x = x + 1
print(ls3)
    

