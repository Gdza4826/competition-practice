# m = int(input())
# n = int(input())
ls = []
ls2 = []
main1= []
main2= []
main3= []
i = 0
for i in range(2):
    matrix = input()
    ls.append(matrix)

for i in ls:
    main1.append(i.split())

for i in main1:
    for x in i:
        number_in_loop = int(x)
        main3.append(number_in_loop)
print(main1)
print(main3)
# for i in range(2):
#     matrix = input()
#     ls2.append(matrix)

# for i in ls2:
#     main2.append(i.split())

# for x,y in zip(main1,main2):
#     result = 0
#     result = x[i] + y[i]
#     i += 1
#     print(result)