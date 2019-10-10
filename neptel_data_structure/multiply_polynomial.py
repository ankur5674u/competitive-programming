
"""

Multiply Polynomial

"""
def multpoly(p1,p2):
    print(p1)
    print(p2)
    import collections
    from itertools import product
    p_sum = collections.Counter()

    for (c1, e1), (c2, e2) in product(p1, p2):
        p_sum[e1 + e2] += c1 * c2
    result = [(coefficient, exponent) for exponent,coefficient in p_sum.items() if coefficient !=0]
    return sorted(result, key=lambda k: k[1], reverse=True)


if __name__ == '__main__':
    multpoly([(1, 1), (-1, 0)], [(1, 2), (1, 1), (1, 0)])