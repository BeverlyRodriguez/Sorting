# Implementing Bubble Sort code.
# Using the array values assigned to me.git add -A

print("\n\t\t\t\t*******PROGRAMMED BY:*******")
print("\t\t\t\t**BEVERLY ANN L. RODRIGUEZ**\n")

print("\t\t   Array values:[60, 63, 96, 5, 90, 43, 75, 41, 99, 23]\n")

def sort(nums):

    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
        print("\t\t", i, "Iterations:  ", numbers)

numbers = [60, 63, 96, 5, 90, 43, 75, 41, 99, 23]
sort(numbers)

# Printing statement for output.
print("\n\n\t\t BUBBLE SORT: ", numbers)