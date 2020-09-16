__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '09-16-2020'

"""
Problem Statement #
Implement a function findMinimum(lst) which finds the smallest number in the given list.

Input: #
A list of integers

Output: #
The smallest number in the list

Sample Input #
arr = [9,2,3,6]
Sample Output #
2
"""


def find_minimum_using_sort(lst):
    """
    This solution sorts the list in ascending order and returns the first element which is also the minimum. We used
    the generic Python .sort() function here, but in a real interview, you should implement your own sort function
    if you’re going to use this solution.

    Also, if the list is empty, None is returned.

    Time Complexity #
    Since most popular sort functions are in O(nlogn), let’s assume that the Python sort function is too. Since we only
    index and return after that, which are constant time operations, this solution takes O(nlogn) time.
    :param lst:
    :return:
    """
    if len(lst) <= 0:
        return None
    lst.sort()  # sort list
    return lst[0]  # return first element


def find_minimum(lst):
    if len(lst) <= 0:
        return None
    minimum = lst[0]
    for ele in lst:
        # update if found a smaller element
        if ele < minimum:
            minimum = ele
    return minimum


if __name__ == "__main__":
    print(find_minimum_using_sort([9, 2, 3, 6]))
    print(find_minimum([9, 2, 3, 6]))
