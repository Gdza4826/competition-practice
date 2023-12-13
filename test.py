# word = input()
# ls1 = []
# ls2 = []
# ls3 = []
# x = 0
# for i in word:
#     ls1.append(i)
# for i in ls1:
#     if i not in ls2:
#         ls2.append(i)
#     elif ls2[(len(ls2)-1)].isdigit():
#         ls2.append(i)
#         break
# print(ls2)
    
num = int(input())
for i in range(num):
    print((" "*(num - (i + 1))) + ("*"*(i+(i+1))))

# Python 3 program to find 
# factorial of given number
# def factorial(n):
# 	return 1 if (n==1 or n==0) else n * factorial(n - 1) 
# num = int(input())
# print("Factorial of",num,"is",factorial(num))

