def gcd(m,n):
    cf = []
    for i in range(1, min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            cf.append(i)
    return (cf[-1])

def improve_gcd(m,n):
    for i in range(1, min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            mrcf = i
    return(mrcf)

def improve_gcd_1(m,n):
    i = min(m,n)
    while i > 0:
        if (m%i) == 0 and (n%i) == 0:
            return(i)
        else:
            i -= 1

# Ecluid's algorithm for gcd using recursion

def euclid_gcd(m,n):
    # Assume m > = n
    if m < n:
        # Swap value m and n
        (m,n) = (n, m)
    if (m%n) == 0:
        return(n)
    else:
        diff = m-n
        # diff >n ? Possible
        return(euclid_gcd(max(n,diff), min(n,diff))) 

# Ecluid Algorithm without recursion

def euclid_gcd_without_recursion(m,n):
    if m < n: # Assume m >= n
        (m,n) = (n,m)

    while (m%n) != 0:
        diff = m-n
        # diff >n > Possible
        (m,n) = (max(diff,n),min(n,diff))
    return n 

#  Actual and improved euclid algorithm

def improved_euclid_gcd(m,n):
    if m < n: # Assume m >= n
        (m,n) = (n,m)
    if (m%n) == 0:
        return(n)
    else:
        return(improved_euclid_gcd(n, m%n)) # m%n < n always!

print("GCD of {} and {} = {} with gcd.".format(50,100,gcd(50,100)))

print("GCD of {} and {} = {} with improve GCD.".format(50,100,improve_gcd(50,100)))

print("GCD of {} and {} = {} with improve GCD 1.".format(50,100,improve_gcd_1(50,100)))

print("GCD of {} and {} = {} with Euclid Algorithm.".format(50,100,euclid_gcd(50,100)))

print("GCD of {} and {} = {} with Euclid Algorithm Without recursion.".format(50,100,euclid_gcd_without_recursion(50,100)))

print("GCD of {} and {} = {} with Actual Euclid Algorithm For GCD.".format(50,100,improved_euclid_gcd(50,100)))
