__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '02-18-2020'


def matrix_sum(mat1, mat2):
    # result = []
    # for i in range(len(mat1)):
    #     temp = []
    #     for j in range(len(mat1[0])):
    #         temp.append(mat1[i][j] + mat2[i][j])
    #     result.append(temp)
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]


def main():
    # Write code here
    m1, n1 = (input().split())
    matrix1 = [list(map(int, input().split(' '))) for i in range(int(m1))]
    m2, n2 = (input().split())
    matrix2 = [list(map(int, input().split(' '))) for i in range(int(m2))]
    result = matrix_sum(matrix1, matrix2)
    for (index, i) in enumerate(result):
        print(" ".join(list(map(str, i))), end='' if index == len(result) - 1 else "\n")


main()

