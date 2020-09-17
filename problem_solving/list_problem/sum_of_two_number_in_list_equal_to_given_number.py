__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '09-16-2020'

"""
Problem Statement #
In this problem, you have to implement the find_sum(lst,k) function which will take a number k as input and return two numbers that add up to k.

Input #
A list and a number k

Output #
A list with two integers a and b that add up to k

Sample Input #
lst = [1,21,3,14,5,60,7,6]
k = 81
Sample Output #
lst = [21,60]

"""


def binary_search(a, item):
    start, end, found, index = 0, len(a) - 1, False, -1
    while start <= end and not found:
        mid = (start + end) // 2
        if a[mid] == item:
            index = mid
            found = True
        else:
            if item < a[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return index


def find_sum_using_brute_force_method(lst, k):
    """
    This is the most time intensive but intuitive solution. Traverse the whole list of size, say s,
    for each element in the list and check if any of the two elements add up to the given number k.
    So, using two nested for-loops each iterating over the entire list will serve the purpose.

    Time Complexity #
    Since we iterate over the entire list of k elements, n times in the worst case, therefore,
     the time complexity is O(n^2)​​.
    :param lst:
    :param k:
    :return:
    """
    # iterate with list i
    for i in range(len(lst)):
        # iterate with j
        for j in range(len(lst)):
            # if sum of two iterators is k
            # and i is not equal to j
            # then we have our answer
            if lst[i] + lst[j] is k and i is not j:
                return [lst[i], lst[j]]
    return False


def find_the_sum_using_sorting_of_list(lst, k):
    """
    While solution #1 is very intuitive, it is not very time efficient. A better way to solve this challenge is by first
    sorting the list. Then for each element in the list, use a binary search to look for the difference between that
    element and the intended sum. In other words, if the intended sum is k and the first element of the sorted list is
    a0, then we will do a binary search for k-a0. The search is repeated for every ai up to an until one is found.”
    You can implement the binary_search() function however you like, recursively or iteratively.

    Time Complexity #
    Since most optimal comparison-based sorting functions take O(nlogn), let’s assume that the Python .sort()
    function takes the same. Moreover, since binary search takes O(logn) time for a finding a single element,
    therefore a binary search for all n elements will take O(nlogn)O(nlogn) time.”
    :param lst:
    :param k:
    :return:
    """
    lst.sort()
    for j in range(len(lst)):
        # find the difference in list through binary search
        # return the only if we find an index
        index = binary_search(lst, k - lst[j])
        if index is not -1 and index is not j:
            return [lst[j], k - lst[j]]
    return False


def find_sum_using_moving_index(lst, k):
    start, end = 0, len(lst) - 1,
    # First of all sort the list
    lst.sort()
    while start != end:
        sum_res = lst[start] + lst[end]
        if sum_res < k:
            start += 1
        elif sum_res > k:
            end -= 1
        else:
            return [lst[start], lst[end]]
    return False


if __name__ == "__main__":
    print(find_sum_using_brute_force_method([1, 21, 3, 14, 5, 60, 7, 6], 81))
    print(find_the_sum_using_sorting_of_list([1, 21, 3, 14, 5, 60, 7, 6], 81))
    print(find_sum_using_moving_index([1, 21, 3, 14, 5, 60, 7, 6], 81))
