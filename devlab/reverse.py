number = input()
ls = number.split(' ')
ls.pop(0)
ls.reverse()
for i in ls:
    print(i,end=' ')