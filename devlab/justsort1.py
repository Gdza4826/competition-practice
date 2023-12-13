ls = []
for i in range(5):
  num = int(input())
  ls.append(num)
ls.sort(reverse=True)
for i in ls:
  print(i)