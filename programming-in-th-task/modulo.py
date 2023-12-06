ls_num = []
ls_cv = []
ls_check = []
for i in range(10):
    number = int(input())
    ls_num.append(number)
for i in ls_num:
    calculate = i % 42
    ls_cv.append(calculate)
for i in ls_cv:
    if i not in ls_check:
        ls_check.append(i)
print(len(ls_check))