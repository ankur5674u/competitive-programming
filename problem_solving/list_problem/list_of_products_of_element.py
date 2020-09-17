__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '09-16-2020'

from functools import reduce  # Required in Python 3
import operator

"""
Problem Statement #
Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.

Input: #
A list of numbers (could be floating points or integers)

Output: #
A list such that each index has a product of all the numbers in the list except the number stored at that index.

Sample Input #
arr = [1,2,3,4]
Sample Output #
arr = [24,12,8,6]
"""


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


def find_product(lst):
    return [prod(lst) // k for k in lst]


def find_product_using_nested_loop(lst):
    """
    This solution iterates over the list and calculates the product of all the numbers to the right of the current
    element as on lines 7 and 8. Then it calculates the product of all the elements to the left of the current element
    line 10. It then multiplies the two products and returns the result line 14.

    Time Complexity #
    This algorithm is in O(n^2) because the list is iterated over n(n-1)/2 times.
    :param lst:
    :return:
    """
    left_prod = 1  # To store product of all previous values from currentIndex
    result = []
    for index, value in enumerate(lst):
        # To store current product for index i
        # current_product = 1
        # compute product of values to the right of index of list
        # current_product * product of all values to the left of i index
        # for ele in lst[index + 1:]:
        #     current_product *= ele
        # result.append(current_product * left_prod)
        # Equivalent statement of line 48, 50, 51, 52 in 54
        result.append(prod((lst[index + 1:])) * left_prod)
        left_prod *= value
    return result


def find_product_using_optimized_multiplication(lst):
    """
    The algorithm for this solution is to first create a new list with products of all elements to the left of each
    element as done on lines 4-6. Then multiply each element in that list to the product of all the elements to the
    right of the list by traversing it in reverse as done on lines 9-11

    Time Complexity #
    Since this algorithm only traverses over the list twice, it’s in linear time, O(n).
    :param lst:
    :return:
    """
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele

    # get product starting from right
    right = 1
    for i in range(len(lst) - 1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product


if __name__ == "__main__":
    print(find_product([1, 2, 3, 4]))
    print(find_product_using_nested_loop([1, 2, 3, 4]))
    print(find_product_using_optimized_multiplication([1, 2, 3, 4]))
