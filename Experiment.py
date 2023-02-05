#Sorting Algos
# 1- Brute force :D

talls = [5,3,2,65,26,85,456,74,34,86,27,96]

for i in range(len(talls)):
    for j in range(len(talls)):
        tmp = 0
        if talls[i] < talls[j]:
            tmp = talls[j]
            talls[j] = talls[i]
            talls[i] = tmp

print(talls)