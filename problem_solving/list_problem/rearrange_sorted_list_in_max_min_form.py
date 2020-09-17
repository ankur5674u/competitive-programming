__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '09-17-2020'

"""
Problem Statement #
Implement a function called maxMin(lst) which will re-arrange the elements of a sorted list such that the 0th index 
will have the largest number, the 1st index will have the smallest, and the third index will have second-largest, 

and so on. In other words, all the odd-numbered indices will have the largest numbers in the list in descending 
order and the even-numbered indices will have the smallest numbers in ascending order.

Input: #
A sorted list

Output: #
A list with elements stored in max/min form

Sample Input #
lst = [1,2,3,4,5]
Sample Output #
lst = [5,1,4,2,3]
"""


def max_min_using_new_list(lst):
    """
    In this solution, we first create a new empty list that we will append the appropriate elements to and return.
    We then iterate through the list starting from the 0th0th index till the middle of the list indexed as
    lst[length(list)/2]. So if the length of the given list is 10, the iterator variable i on line 4 in our
    solution would start from 0 and end at 10/2 = 510/2=5. Note that the starting index 0 in the example
    is inclusive, and the ending index 5 is exclusive. At each iteration, we first append the largest
    unappended element and then the smallest. So in the first iteration, i = 0 and lst[-(0+1)] = lst[-1]
    corresponds to the last element of the list, which is also the largest. So the largest element in
    the list is appended to result first, and then the current or element indexed by i is appended. Next,
    the second largest and the second smallest are appended and so on until the end of the list.

    Time Complexity #
    The time complexity of this problem is O(n) as the list is iterated over once.
    :param lst:
    :return:
    """
    # Iterate over half of the array
    result = []
    for i in range(len(lst) // 2):
        # First add max element in the list
        result.append(lst[-(i + 1)])
        # Add min element
        result.append(lst[i])
    # if middle value then append
    if len(lst) % 2 == 1:
        result.append(lst[len(lst) // 2])
    return result


def max_min(lst):
    """
    This solution uses some math to store two elements at one index. This is achieved from the following line of
    code,

        lst[i] += (lst[max_index] % max_element) * max_element

    lst[max_index] is stored as a multiplier and lst[i] is stored as remainder.
    For example in the list, [1, 2, 3, 4, 5, 6, 7, 8, 9], the max_element is 1010 and 9191 is stored at index 00.
    One we have 9191, we can get the new element 99 using 91/1091/10. Also, we can go back to the original
    element, 1, using the expression 91%10.

    This allows us to swap the numbers in place without using any extra space. To get the final list,
    we simply divide each element by max_element as done in the last for loop.

    Note: This approach only works for non-negative numbers!

    Time Complexity #
    The time complexity of this solution is in O(n). The space complexity is constant.


    :param lst:
    :return:
    """
    # Return empty list for empty list
    if len(lst) is 0:
        return []

    max_index = len(lst) - 1  # max index
    min_index = 0  # first index
    max_element = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[max_index] % max_element) * max_element
            max_index -= 1
        # odd number means min number
        else:
            lst[i] += (lst[min_index] % max_element) * max_element
            min_index += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // max_element
    return lst


if __name__ == "__main__":
    print(max_min_using_new_list([1, 2, 3, 4, 5]))
