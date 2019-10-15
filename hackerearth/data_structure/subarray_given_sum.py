def sub_array_sum(arr, sum):
    curr_sum = arr[0]
    left_pointer = 0
    right_pointer = 1
    while right_pointer <= len(arr):
        # current sum == given sum
        if curr_sum == sum:
            return dict(index=(left_pointer, right_pointer - 1), sub_array=arr[left_pointer:right_pointer])
        if right_pointer < len(arr):
            curr_sum += arr[right_pointer]

        while curr_sum > sum and left_pointer < right_pointer - 1:
            curr_sum -= arr[left_pointer]
            left_pointer += 1

        right_pointer += 1
    return -1


if __name__ == '__main__':
    array = [1, 4, 20, 3, 10, 5]
    sum = 333
    print(sub_array_sum(array, sum))
