#START

# Implementing Insertion Sort code.
# Using the array values assigned to me.


print("\n\t\t\t\t*******PROGRAMMED BY:*******")
print("\t\t\t\t**BEVERLY ANN L. RODRIGUEZ**\n")


print("\t\t   Array values:[60, 63, 96, 5, 90, 43, 75, 41, 99, 23]\n")

def insertion_Sort(numbers):
    for i in range(1,len(numbers)):
        sorted_area = numbers[i]
        j = i - 1
        while j >= 0 and sorted_area < numbers[j]:
            numbers[j+1] = numbers[j]
            j = j - 1
        numbers[j+1] = sorted_area
        print("\t\t", i, "Iterations:  ", numbers)
   

numbers = [60, 63, 96, 5, 90, 43, 75, 41, 99, 23]
insertion_Sort(numbers)

print("\n\n\t\tINSERTION SORT: ", numbers)

