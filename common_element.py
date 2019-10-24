#Common Elements in Two Sorted Arrays
#Write a function that returns the common elements (as an array) between two sorted arrays of integers (ascending order).
#Example: The common elements between [1, 3, 4, 6, 7, 9] and [1, 2, 4, 5, 9, 10] are [1, 4, 9].
#O(max(n,m)) where n is the number of items of the first array and m the number of items of the second array
#REMINDER: We're going to use lists instead of arrays in Python for simplicity.


# Function implementation.
def common_elements(list1, list2):
    result = []
    index1 = 0
    index2 = 0
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] == list2[index2]:
            result.append(list1[index1])
            index1 += 1
            index2 += 1
        elif list1[index1] > list2[index2]:
            index2 += 1
        else:
            index1 += 1
    return result


# NOTE: The following input values will be used for testing your solution.
list_a1 = [1, 3, 4, 6, 7, 9]
list_a2 = [1, 2, 4, 5, 9, 10]
# common_elements(list_a1, list_a2) should return [1, 4, 9] (a list).
list_b1 = [1, 2, 9, 10, 11, 12]
list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
# common_elements(list_b1, list_b2) should return [1, 2, 9, 10, 12] (a list).
list_c1 = [0, 1, 2, 3, 4, 5]
list_c2 = [6, 7, 8, 9, 10, 11]
# common_elements(list_c1, list_c2) should return [] (an empty list).

result = common_elements(list_b1, list_b2)
print(result)
result = common_elements(list_a1, list_a2)
print(result)
result = common_elements(list_c1, list_c2)
print(result)