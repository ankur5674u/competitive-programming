"""

https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/memorise-me/

"""

# Write your code here
from collections import Counter

# Total number of numbers in your team
number_count = int(input())
# Number List in python
number_list = [int(x) for x in input().split()]
# Query count
query_count = int(input())
arr = Counter(number_list)
for i in range(0, query_count):
    query_number = int(input())
    print(arr[query_number] if arr[query_number] != 0 else 'NOT PRESENT')

