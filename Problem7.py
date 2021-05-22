"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

# All primes > 3 are of the form 6k+1 or 6k-1 where k is an integer > 0
# This is used to check the primality of the integer and then Nth prime number is found
def CheckPrime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def NthPrimeGeneration(n):
    count = 0
    i = 0
    while count != n:
        if CheckPrime(i) == True:
            count += 1
            i += 1
        else:
            i += 1
    return i-1

print(NthPrimeGeneration(10001))
