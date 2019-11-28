def merge_sort(arr):
    # Finding mid position
    if len(arr) > 1:
        mid = len(arr) // 2
        #  Dividing array in two half
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)
        # merging two array
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[i]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking any element left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1




# Code to print the list
def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    print_list(arr)
    merge_sort(arr)
    print("Sorted array is: ", end="\n")
    print_list(arr)
