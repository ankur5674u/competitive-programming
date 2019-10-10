"""

Add Polynomial py

"""

def addpoly(p1,p2):
    import collections
    p_sum = collections.Counter()
    for coefficient , exponent in (p1 + p2):
        p_sum[exponent] += coefficient
    result = [(coefficient, exponent) for exponent,coefficient in p_sum.items() if coefficient !=0]
    return sorted(result, key=lambda k: k[1], reverse=True)


if __name__ == '__main__':
    addpoly([(4, 3), (3, 0)], [(-4, 3), (2, 1)])