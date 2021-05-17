"""
Problem 3 - Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def LargestPrimeFactor(number):
    arr = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            arr.append(divisor)
            number = number/divisor
        else:
            divisor += 1
    return max(arr)

print(LargestPrimeFactor(600851475143))
        