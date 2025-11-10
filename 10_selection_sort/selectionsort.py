import random

arr = []
selection_sort = []
for i in range(10):
    arr.append(random.randint(0,100))

print(arr)
var = 0
for i in range(len(arr)):
    var = max(arr)
    selection_sort.append(var)
    arr.remove(var)

print(selection_sort)

