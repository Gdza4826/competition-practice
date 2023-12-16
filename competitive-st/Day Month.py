Day = int(input("Day : "))
Month = int(input("Month : "))

list_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
             "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if Day < 1:
    print("Error")
elif Month in [1,3,5,7,8,10,12] and Day > 31:
    print("Error")
elif Month in [4,6,9,11] and Day > 30:
    print("Error")
elif Month == 2 and Day > 29:
    print("Error")
else:
    Day1 = Day % 7
    if Month in [9,12]:
        print(list_week[Day1 - 1])

    elif Month in [1,4,7]:
        print(list_week[Day1])

    elif Month in [10]:
        print(list_week[Day1 + 1])

    elif Month in [5]:
        print(list_week[Day1 + 2])

    elif Month in [2,8]:
        print(list_week[Day1 + 3])

    elif Month in [3,11]:
        print(list_week[Day1 + 4])

    elif Month in [6]:
        print(list_week[Day1 + 5])
    else:
        print("Error")




