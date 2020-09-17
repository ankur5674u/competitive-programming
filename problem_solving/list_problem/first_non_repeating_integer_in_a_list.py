__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '09-16-2020'

"""
Problem Statement #
Implement a function, find_first_unique(lst) that returns the first unique integer in the list.

Input #
A list of integers

Output #
The first unique element in the list

Sample Input #
[9,2,3,2,6,6]
Sample Output #
9
"""


def find_first_unique(lst):
    """
    We start with the first element of the list and compare it with all the other elements while traversing the list.
    If no other same element with the same value is found, then this is the first non-repeating element in the list
    (9 in our example). If, however, a similar element is found, we skip to the second element of the list to check if
    it is unique. The process gets repeated for the entire list.

    Time Complexity #
    The time complexity of this solution is O(n^2) since the entire list is iterated n times for each element→ nn×nn
    :param lst:
    :return:
    """
    for index1 in range(len(lst)):
        index2 = 0
        # iterate the second list using index2
        while index2 < len(lst):
            if index1 != index2 and lst[index1] == lst[index2]:
                break
            index2 += 1
        if index2 == len(lst):
            return lst[index1]
    return None


if __name__ == "__main__":
    print(find_first_unique([9, 2, 3, 2, 6, 6]))
    print(find_first_unique([9, 2, 3, 2, 6, 6]))
