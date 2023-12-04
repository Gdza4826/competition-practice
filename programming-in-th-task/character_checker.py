word = input()
ls = []
for i in word:
    ls.append(i)
ls.sort()
counter = len(ls)
if ls[0].isupper() and ls[counter-1].isupper():
    print("All Capital Letter")
elif ls[0].islower() and ls[counter-1].islower():
    print("All Small Letter")
else:
    print("Mix")