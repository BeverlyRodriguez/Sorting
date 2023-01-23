# Implementing Quick Sort code.
# Using the array values assigned to me.


print("\n\t\t\t\t*******PROGRAMMED BY:*******")
print("\t\t\t\t**BEVERLY ANN L. RODRIGUEZ**\n")


print("\t\t   Array values:[60, 63, 96, 5, 90, 43, 75, 41, 99, 23]\n")
def quicksort(numbers,left,right):
    if left < right:
        partition_pos = partition(numbers,left,right)
        quicksort(numbers, left,  partition_pos - 1)
        quicksort(numbers, partition_pos + 1, right)

def partition(numbers, left, right):
    i = left
    j = right - 1
    pivot = numbers[right]

    while i < j:
        while i < right and numbers[i] < pivot:
            i += 1
        while j > left and numbers[j] >= pivot:
            j-=1

        if i < j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            print("\t\t\t ", numbers)

    if numbers[i] > pivot:
        numbers[i], numbers[right] = numbers[right], numbers[i]
        print("\t\t\t ", numbers)
    return i
    


numbers = [60, 63, 96, 5, 90, 43, 75, 41, 99, 23]
quicksort(numbers, 0, len(numbers) - 1)

print("\n\n\t\t  QUICK SORT: ", numbers)
