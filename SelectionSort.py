# Implementing Selection sort code.
# Using the array values assigned to me.


print("\n\t\t\t\t*******PROGRAMMED BY:*******")
print("\t\t\t\t**BEVERLY ANN L. RODRIGUEZ**\n")

print("\t\t   Array values:[60, 63, 96, 5, 90, 43, 75, 41, 99, 23]\n")

def sort(numbers):

   for i in range(9):
    minpos = i
    for j in range (i,10):
        if numbers[j] < numbers[minpos]:
            minpos = j

    # For the array values to swap.
    temp = numbers[i]
    numbers[i] = numbers[minpos]
    numbers[minpos] = temp
    print("\t\t\t ", numbers)

numbers = [60, 63, 96, 5, 90, 43, 75, 41, 99, 23]
sort(numbers)

# Printing statement for output.
print("\n\n\t\tSELECTION SORT: ", numbers)


