def NumberSum(n):
    result = ''
    ls_debug_one = []
    ls_debug_two = []
    for i in n:
        convert = int(i)
        ls_debug_one.append(convert)
    total = sum(ls_debug_one)
    convertToStr = str(total)
    result = convertToStr
    checker = len(result)
    if checker == 1:
        print(total)
    else:
        NumberSum(result)

n = NumberSum('123456')

# n = '15'       
# result = ''
# ls_debug_one = []
# ls_debug_two = []
# for i in n:
#     convert = int(i)
#     ls_debug_one.append(convert)
# total = sum(ls_debug_one)
# convertToStr = str(total)
# result = convertToStr
# checker = len(result)
# print(checker)
