"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def pythagoreanTriplet(n):

    # If the triplets are in sorted order.
    # The value of first element in the triplet will be at-most n/3.
    for i in range(1, int(n / 3) + 1):

        # The value of second element will be less than equal to n/2
        for j in range(i + 1, int(n / 2) + 1):
            k = n - i - j
            if (i * i + j * j == k * k):
                print(i, ", ", j, ", ", k, sep = "")
                return i*j*k
    print("No Triplet")

n = 1000
print(pythagoreanTriplet(n))
