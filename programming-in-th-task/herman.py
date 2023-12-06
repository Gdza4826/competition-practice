x1ands = input()
ls_sp = x1ands.split()
ls_cvd = []
for i in ls_sp:
    cv = int(i)
    ls_cvd.append(cv)
total = (ls_cvd[1]*2) - ls_cvd[0]
print(total)