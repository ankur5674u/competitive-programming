__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '07-27-2020'


def longest_common_subsequence(x, y):
    len_x = len(x)
    len_y = len(y)
    # Declaring 2d array for storing result
    result = [[-1] * (len_y + 1) for i in range(len_x + 1)]
    for i in range(len_x + 1):
        for j in range(len_y + 1):
            if i == 0 or j == 0:
                result[i][j] = 0
            elif x[i-1] == y[j-1]:
                result[i][j] = 1 + int(result[i - 1][j - 1])
            else:
                result[i][j] = max([result[i][j - 1], result[i - 1][j - 1]])
    for i in range(len_x + 1):
        for j in range(len_y + 1):
            print(f"{result[i][j]} ", end='')
        print("")
    return result[len_x][len_y]


if __name__ == "__main__":
    X = "bd"
    Y = "abcd"
    print("Length of LCS is ", longest_common_subsequence(X, Y))
