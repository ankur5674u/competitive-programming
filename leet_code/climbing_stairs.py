__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '07-27-2020'

"""
https://leetcode.com/problems/climbing-stairs/

"""


class Solution:
    @staticmethod
    def climb_stairs(n: int) -> int:
        # USING RECURSION
        if n == 0 or n == 1:
            return 1
        return Solution.climb_stairs(n - 1) + Solution.climb_stairs(n - 2)

    @staticmethod
    def climb_stairs_1(n: int) -> int:
        """
        climb_stairs() is really slow (O(N^2) --- we are doing a lot of repeated computations!
        We can do it a lot faster by just computing iteratively:
        :param n:
        :return:
        """
        a, b = 1, 2

        for _ in range(n - 1):
            a, b = b, a + b
            print(a, b)
        return a

    @staticmethod
    def climb_stairs_2(n: int) -> int:
        """
        :param n:
        :return:
        """
        if n == 0 or n == 1:
            return 1
        cache = [-1] * (n + 1)
        cache[0], cache[1] = 1, 1
        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[-1]

    @staticmethod
    def climb_stairs_3(n: int, step_type: tuple) -> int:
        """
        :param n:
        :param step_type:
        :return:
        """
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif n in step_type:
            return 1 + sum(Solution.climb_stairs_3(n - x, step_type) for x in step_type if x < n)
        else:
            return sum(Solution.climb_stairs_3(n - x, step_type) for x in step_type if x < n)

    @staticmethod
    def climb_stairs_4(n: int, step_type: tuple) -> int:
        """
        :param n:
        :param step_type:
        :return:
        """
        cache = [0] * (n + 1)
        cache[0] = 1
        for i in range(n + 1):
            cache[i] += sum(cache[i - x] for x in step_type if i - x > 0)
            cache[i] += 1 if i in step_type else 0
        return cache[-1]


if __name__ == '__main__':
    print(Solution.climb_stairs(3))
