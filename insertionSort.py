
def insertion_sort(arr):
    # loop through n-1 elements
    # we need to have the left side of the array be our "sorted array"
    for i in range(1, len(arr)):
        temp = arr[i]  # at the start, it would be array[1]
        j = i

        while j > 0 and temp < arr[j - 1]: # always check if the element before j is in the right spot
            # shift left until correct position is found
            arr[j] = arr[j - 1]
            j -= 1
            # insert at correct position
        arr[j] = temp
    return arr

print(insertion_sort([4, 3, 10, 6, 5]))



numbers = [5,6,27,2,57,1,4,7,21,753,86453,243,7,23,4,132,7485434,1412,31234]


def insertion_sort2(arr):
    for x in range(1, len(arr)):
        curNum = arr[x]
        for y in range(x-1, 0, -1):
            if arr[y] > curNum:
                arr[y+1] = arr[y]
            else:
                arr[y+1] = curNum
                break
    return arr


print(insertion_sort2(numbers))