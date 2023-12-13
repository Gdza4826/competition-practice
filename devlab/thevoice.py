num = input()
dict01 = {
    "K":'',
    "K1":'',
    "K2":'',
    "S1":'',
    "S2":'',
    "G":''
}
ls_num = num.split(' ')
for x,y in zip(ls_num,dict01):
    dict01[y] = x
if dict01['K1'] == dict01['K']:
    print('2')
elif dict01['K2'] == dict01['K']:
    print('1')
else:
    if int(dict01['S1']) <= 8 or int(dict01['S2']) <= 8:
        print('0')
    else:
        if dict01['G'] == '1':
            print('1')
        else:
            print('2')