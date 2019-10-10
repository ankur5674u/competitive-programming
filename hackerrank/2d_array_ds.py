"""

https://www.hackerrank.com/challenges/2d-array/problem


"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum=-9 * 7
    for row in range(len(arr)-2):
        for col in range(len(arr[row])-2):
            hour_sum = sum([arr[row][col], arr[row][col+1],arr[row][col+2],
                            arr[row+1][col+1],
                            arr[row+2][col], arr[row+2][col+1], arr[row+2][col+2]])
            max_sum=max(max_sum,hour_sum)
    return max_sum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
