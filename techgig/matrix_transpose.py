__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '02-18-2020'


def transpose_matrix(mat):
    for i in range(len(mat)):
        for j in range(i + 1, len(mat)):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat


if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m = transpose_matrix(mat)
    print(m)
