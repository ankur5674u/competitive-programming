__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '09-17-2020'

"""
Problem Statement #
Implement a function right_rotate(lst, n) which will rotate the given list by k. This means that the right-most elements will appear at the left-most position in the list and so on. You only have to rotate the list by one element at a time.

Input #
A list and a number by which to rotate that list

Output: #
The given list rotated by k elements

Sample Input #
lst = [10,20,30,40,50]
n = 3
Sample Output #
lst = [30,40,50,10,20]
"""


def rotate_right_list(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]


def right_rotate(lst, n):
    """
    In this solution, we first create an empty list. We then iterate through the last k elements of the list and
    place them at the start of the new list. Lastly, we append the first length(lst)-k elements to the new list
    and return.

    Time Complexity #
    Since the entire list is iterated over, the time complexity of this solution is O(n)
    :param lst:
    :param n:
    :return:
    """
    n = n % len(lst)
    rotated_list = []
    # get the elements from the end
    for item in range(len(lst) - n, len(lst)):
        rotated_list.append(lst[item])
    # get the remaining elements
    for item in range(0, len(lst) - n):
        rotated_list.append(lst[item])
    return rotated_list


if __name__ == "__main__":
    print(rotate_right_list([10, 20, 30, 40, 50], 3))
    print(right_rotate([10, 20, 30, 40, 50], 3))
