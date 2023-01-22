#Start
numbers = [60, 63, 96, 5, 90, 43, 75, 41, 99, 23]
def sort(numbers):
   for i in range(10):
    minpos = i
    for j in range (i,11):
        if numbers[j] <numbers [minpos]:
            minpos = j

    #For the array values to swap.
    temp = numbers[i]
    numbers [i] = numbers [minpos]
    numbers[minpos] = temp
    

