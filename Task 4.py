# Task 2: sum of numbers from 1 to 50 using for loop.
n = 0
l = list(range(1,51))
for i in l:
    n = n + i
print("The sum of numbers from",l[0],"to",l[-1], "is:",n)