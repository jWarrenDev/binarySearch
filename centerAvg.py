# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array.

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

numbers = [1,2,3,4,100]
numbers2 = [1,2,3,5,89,00]
numbers3 = [1,5.,46,4,362,3,24662]

def centered_average(array):
    # largest = max(array)
    # smallest = min(array)

    # return largest, smallest

    sorted_array = sorted(array)

    sliced = sorted_array[1: -1]

    sum = 0
    for num in sliced:
        sum += num
        return sum / len(sliced)


print(centered_average(numbers))
print(centered_average(numbers2)) 

print(centered_average(numbers3)