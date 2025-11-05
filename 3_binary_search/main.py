list= ["apples", "bananas", "blueberries",
       "cherries", "cantaloupes","dates", "figs",
       "grapes","kiwis", "mangos"]
item = input("Enter an fruit: ")

def binarysearch(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return f"item is found : {guess}"
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return print(f"Sorry {item} was not found")

print(binarysearch(list, item))
