"""
https://www.hackerrank.com/challenges/python-time-delta/problem

"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the time_delta function below.
def time_delta(t1, t2):
    from datetime import datetime
    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return int(abs((t1 - t2).total_seconds()))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for _ in range(int(input())):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        fptr.write(str(delta) + '\n')

    fptr.close()
