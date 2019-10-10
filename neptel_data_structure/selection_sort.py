def SelectionSort(l):
    # Scan slices l[0:len(l)], l[1:ken(l)]
    for start in range(len(l)):
        # Find the minium value in slice
        minpos = start
        for i in range(start, len(l)):
            if l[i] < l[minpos]:
                minpos = i
                #  move it start of the slice
        (l[start], l[minpos]) = (l[minpos], l[start])


if __name__ == '__main__':
    SelectionSort([74, 32, 89, 55, 21, 64])
