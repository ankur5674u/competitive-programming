__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '09-16-2020'
"""
Implement a function that merges two sorted lists of m and n elements respectively,
into another sorted list. Name it merge_lists(lst1, lst2).

Input #
Two sorted lists.

Output #
A merged and sorted list consisting of all elements of both input lists.

Sample Input #
list1 = [1,3,4,5]  
list2 = [2,6,7,8]
Sample Output #
arr = [1,2,3,4,5,6,7,8]
"""


def merge_lists(lst1, lst2):
    x, y = 0, 0
    while x < len(lst1) and y < len(lst2):
        if lst1[x] > lst2[y]:
            lst1.insert(x, lst2[y])
            x += 1
            y += 1
        else:
            x += 1
    if y < len(lst2):
        lst1.extend(lst2[y:])

    return lst1


def merge_two_sorted_list(l1, l2):
    l1_index, l2_index, result_index = 0, 0, 0
    result = []
    while l1_index < len(l1) and l2_index < len(l2):
        if l1[l1_index] < l2[l2_index]:
            result.insert(result_index, l1[l1_index])
            l1_index += 1
            result_index += 1
        else:
            result.insert(result_index, l2[l2_index])
            l2_index += 1
            result_index += 1
    while l1_index < len(l1):
        result.insert(result_index, l1[l1_index])
        l1_index += 1
        result_index += 1
    while l2_index < len(l2):
        result.insert(result_index, l2[l2_index])
        l2_index += 1
        result_index += 1
    return result
