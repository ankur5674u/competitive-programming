__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '09-17-2020'

"""
Problem Statement #
Implement a function find_second_maximum(lst) which returns the second largest element in the list.

Input: #
A List

Output: #
Second largest element in the list

Sample Input #
[9,2,3,6]
Sample Output #
6
"""


def find_second_maximum_using_sorting(lst):
    """
    Time Complexity #
    The time complexity of this solution depends on the running time of sort() function. Assuming that Python sort()
    function runs in an optimal time of O(nlogn)O(nlogn), our solution also takes O(nlogn)O(nlogn) time."

    Caveat: Note that this solution won’t work if duplicates of the first largest number exist. For instance,
    it would not work with a list like [1,2,4,4] since it would return 4 which is at the second last index of the
    sorted list. But, it is the largest element and not the correct answer.
    :param lst:
    :return:
    """
    lst.sort()
    if len(lst) >= 2:
        return lst[-2]
    else:
        return None


def find_second_maximum_traversing_the_list_twice(lst):
    if len(lst) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for item_value in lst:
        if item_value > max_num:
            max_num = item_value
    for item_value in lst:
        if max_num > item_value > second_max_num:
            second_max_num = item_value
    return second_max_num


def find_second_maximum_number_in_single_iteration(lst):
    if len(lst) < 2:
        return None
    # initialize two variable to infinity
    max_num = second_max_num = float('-inf')
    for item_value in lst:
        # Update the max value, if max value is found
        if item_value > max_num:
            second_max_num = max_num
            max_num = item_value
        elif item_value > second_max_num and item_value != max_num:
            second_max_num = item_value
    return second_max_num if second_max_num != float('-inf') else None


if __name__ == "__main__":
    print(find_second_maximum_using_sorting([9, 2, 3, 2, 6, 6]))
    print(find_second_maximum_traversing_the_list_twice([9, 2, 3, 2, 6, 6]))
    print(find_second_maximum_number_in_single_iteration([9, 2, 3, 2, 6, 6]))
