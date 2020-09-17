__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '09-17-2020'

"""
Problem Statement #
Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear on the left and positive elements appear at the right of the list. Note that it is not necessary to maintain the sorted order of the input list.

Generally zero is NOT positive or negative, we will treat zero as a positive integer for this challenge! So, zero will be placed at the right.

Output #
A list with negative elements at the left and positive elements at the right

Sample Input #
[10,-1,20,4,5,-9,-6]
Sample Output #
[-1,-9,-6,10,20,4,5]
"""


def rearrange_using_auxiliary_list(lst):
    """
    In this solution, we use two auxiliary lists, neg and pos, to store negative and positive elements respectively.
    We then iterate over the entire input list and append negative elements to one list and the positive ones to the
    other. Finally, we simply join both auxiliary lists and return.

    Time Complexity #
    Since the given list is only iterated over once, the time complexity of this solution is O(n)

    :param lst:
    :return:
    """
    neg = []
    pos = []
    # make a list of negative and positive numbers
    for ele in lst:
        if ele < 0:
            neg.append(ele)
        else:
            pos.append(ele)
    # merge two lists and return
    return neg + pos


def rearrange_in_place(lst):
    """
    In this solution, we iterate over the entire list and, if we encounter a negative element, we simply swap it
    with the leftmost positive element.

    Time Complexity #
    The time complexity of this algorithm is O(n) as the entire list is iterated over once, with no extra space used.
    :param lst:
    :return:
    """
    start = 0
    for curr_index, value in enumerate(lst):
        if value < 0:
            if curr_index is not start:
                # SWAP THEM
                lst[curr_index], lst[start] = lst[start], lst[curr_index]
            # Update the lst position
            start += 1
    return lst


def rearrange(lst):
    # get negative and positive list after filter and then merge
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]


if __name__ == "__main__":
    print(rearrange_using_auxiliary_list([10, -1, 20, 4, 5, -9, -6]))
    print(rearrange_in_place([10, -1, 20, 4, 5, -9, -6]))
    print(rearrange([10, -1, 20, 4, 5, -9, -6]))
