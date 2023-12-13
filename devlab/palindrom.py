number = input()
debug_checker = 0
ls1 = []
ls2 = []
debug1 = "";
debug2 = "";
ls3 = []
ls4 = []
for i in number:
    ls1.append(i)
    ls2.append(i)
while (debug_checker == 0):
    ls2.reverse()
    for i in ls1:
        debug1 += i
    for i in ls2:
        debug2 += i
    total = int(debug1)+int(debug2)
    for i in str(total):
        ls3.append(i)
        ls4.append(i)
    ls4.reverse()
    if ls3 == ls4:
        print(total)
        debug_checker = 1
    else:
        ls1 = []
        ls2 = []
        if len(debug2) == 30:
            print("-1")
            break
        else:
            debug1 = ""
            debug2 = ""
            ls1.extend(ls3)
            ls2.extend(ls3)
            ls3 = []
            ls4 = []
