import random
import time



# sorted list is a must
# Binary search ~ O(log(n)), naive search ~ O(n)


# naive search: scan entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# binary search uses divide and conquer!
# we will leverage the fact that our list is SORTED

def binary_search(l, target, low = None, high =None):
    if low is None:
        low = 0
    if high is None:
        high = (len(l) - 1)

    if high < low:
        return -1

    mid_point = (low + high) // 2

    if l[mid_point] == target:
        return mid_point

    elif target < l[mid_point]:
        return binary_search(l, target, low, mid_point - 1)
    else:
        #target > l[mid_point]:
        return binary_search(l, target, mid_point + 1, high)

if __name__ == '__main__':
    #list = [1,3,5,10,12]
    # target = 7
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    #build a sorted list of length 10000
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end= time.time()
    print("Naive search time: ", (end-start), "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start), "seconds")










