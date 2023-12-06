# A < B , B < C ... C most , B , A lessest
num_input = input()
charector = input()
ls_num = num_input.split()
ls_num_cv = []
ls_char_cv = []
for i in ls_num:
    cv_db = int(i)
    ls_num_cv.append(cv_db)
for i in charector:
    ls_char_cv.append(i)