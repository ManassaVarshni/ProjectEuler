"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
# METHOD 1

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

sum = 0
for i in range(1,2000000):
    if CheckPrime(i) == True:
        sum += i
print(sum)

# METHOD 2

# Since method 1 is slower, Sieve of Eratosthenes is implemented to find the prime numbers

import numpy as np

n = 5000000
sieve_arr = np.array([True for _ in range(n)])
sieve_arr[0:2] = False
upper_bound = int(np.sqrt(n))

for i in range(2, upper_bound+1):
    if sieve_arr[i]:
        j = i * i
        count = 0
        while j < n:
            sieve_arr[j] = False
            j = (i * i) + (count * i)
            count += 1

prime_arr = np.where(sieve_arr == True)[0]

ind = np.where(prime_arr < 2000000)[0]
subset = prime_arr[ind]
solution = sum(subset)
print(solution)
