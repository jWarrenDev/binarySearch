data = [2,34,7,8,9, 12, 14,17,19,22,25,27,28,33,37]
target = 25

print(data)

#Linear search

def linear_search(data,target):
    for x in range(len(data)):
        if data[x] == target:
            return True
    return False

print(linear_search(data,target)) # Returns True


def binary_search(data, targeg):
    low = 0
    high = len(data) -1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

print(binary_search(data, target))


#recursive

def recursive(data, target, low, high):
    if low > high:
        return False
    else: 
        mid = (low +  high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return recursive(data, target, low, mid-1)
        else:
            return recursive(data, target, mid-1, high)

print(recursive(data, target, 0, len(data) -1))


# start by choosing a pivot
# this can be the first or last element
# the middle, median, or random element usually performs better (tends to split the original data more evenly)
# b. Move all elements smaller than the pivot to its left hand side. move all elements larger than pivot to its right hand side.
# c. recursively quick sort LHS and RHS until (some base case) where a side only contains a single element
# sorted_thingy [1][2] [3][4][5][6]


def partition(data):
    left = []
    pivot = data[0]
    right = []
    for variable in data[1:]:
        if variable <= pivot:
            left.append(variable)
        else:
            right.append(variable)
    return left, pivot, right


def quicksort(data):
    if data == []:
        return data
    left, pivot, right = partition(data)
    return quicksort(left) + [pivot] + quicksort(right)
    
print(quicksort([5, 9, 3, 7, 2, 8, 1, 6]))

