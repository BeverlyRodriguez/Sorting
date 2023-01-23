# Implementing Merge Sort code.
# Using the array values assigned to me.


print("\n\t\t\t\t*******PROGRAMMED BY:*******")
print("\t\t\t\t**BEVERLY ANN L. RODRIGUEZ**\n")

print("\t\t   Array values:[60, 63, 96, 5, 90, 43, 75, 41, 99, 23]\n")


def merge_sort (Numbers):
    if len(Numbers) > 1:
        # Dividing into two parts
        LeftPart = Numbers[:len(Numbers)//2]
        RightPart = Numbers[len(Numbers)//2:]

        merge_sort(LeftPart)
        merge_sort(RightPart)

        
numbers = [60, 63, 96, 5, 90, 43, 75, 41, 99, 23]