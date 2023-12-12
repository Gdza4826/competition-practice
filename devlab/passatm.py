word = input()
debug_checker = 0
ls = []
for i in word:
    if i.isdigit():
        debug_checker = debug_checker*10 + int(i)
    else:
        if debug_checker != 0:
            ls.append(debug_checker)
            debug_checker = 0
ls_sp = []
for i in word:
    ls_sp.append(i)
if ls_sp[(len(ls_sp)-1)].isdigit():
    check_int = int(ls_sp[(len(ls_sp)-1)])
    ls.append(check_int)
total = sum(ls)
if total < 1000:
    check = len(str(total))
    print('0'*check,end='')
    print(total)
else:
    print(total)