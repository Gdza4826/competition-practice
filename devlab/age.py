number = input()
ls = number.split(' ')
ls_cv = []
for i in ls:
    cv = int(i)
    ls_cv.append(cv)
B = (ls_cv[0]//(ls_cv[1]-1))+ls_cv[2] # B = ( N / (M - 1) ) + Y
A = ls_cv[0] + B # A = N + B
print(A,end=' ')
print(B)