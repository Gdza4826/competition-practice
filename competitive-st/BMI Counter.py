weight_list = []
height_list = []
result_list = []
counter = 0
while True:
    weight = int(input())
    height = int(input())
    if weight <= 0 or height <= 0:
        break
    else:
        convert_to_m = height / 100
        weight_list.append(weight)
        height_list.append(convert_to_m)

for x,y in zip(weight_list,height_list):
    bmi_cl = x / (y * y)
    result_list.append(bmi_cl)

for i in result_list:
    if i < 18.5:
        counter += 1

print("BMI < 18.5 =",counter)
