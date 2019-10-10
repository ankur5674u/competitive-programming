import numpy as np


def matrixflip(m, d=None):
    k = m
    if d == "h":
        for i in range(len(k)):
            k[i] = k[i][::-1]
            # for j in range(len(m[i])):
        return k
    elif d == 'v':
        return list(list(x)[::-1] for x in zip(*matrix))
    else:
        return m


def transpose(matrix_a):
    for row in matrix_a:
        print(row)
    transpose_matrix = [[matrix_a[j][i] for j in range(len(matrix_a))] for i in range(len(matrix_a[0]))]
    #     transpose_matrix = map(list, zip(*matrix_a))
    return transpose_matrix


def descending(integer_list):
    for i in range(0, len(integer_list) - 1):
        if integer_list[i] < integer_list[i+1]:
            return False
    return True

def valley(integer_list):
    valley_flag = False
    for i in range(0,len(integer_list)-1):
#         print (integer_list[i])
        if integer_list[i] == integer_list[i+1]:
            return False
        if not valley_flag:
            if integer_list[i] > integer_list[i+1]:
                continue
            if integer_list[i] < integer_list[i+1]:
                valley_flag = True
        else:
            if integer_list[i] > integer_list[i+1]:
                return False
            elif integer_list[i] < integer_list[i+1]:
                continue
    return valley_flag


if __name__ == '__main__':
    matrixflip([[1, 2], [3, 4]], 'h')
    descending([4, 4, 3])
    valley([3, 2, 1, 2, 3])
    transpose([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
