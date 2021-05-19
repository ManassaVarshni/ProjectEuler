"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
# LCM of n numbers has been found using 2 methods - Brute force method and a more optimised method

# METHOD 1

# Function to find the GCD of two numbers
def GCD(a,b):
    gcd = 1
    num = 2
    if a>b:
        greater = a
    else:
        greater = b
    while num < greater/2:
        if a%num == 0 and b%num == 0:
            gcd = gcd*num
            a = a/num
            b = b/num
        else:
            num += 1
    return gcd

# LCM(a,b) = a*b/GCD(a,b)
def LCM(a,b):
    lcm = (a*b)/GCD(a,b)
    return lcm

# Function to reduce the LCM(1,2,3,...20) to LCM(result,20)
def LCM_Of_n_Num(n):
    answer = LCM(1,2)
    b = 3
    while b != 20:
        answer = LCM(answer, b)
        b += 1
    return answer

print(LCM_Of_n_Num(20))


# METHOD 2

# Function to find the GCD of two numbers using Euclidean algorithm
def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

# Function to find LCM of n numbers
def LCM(n):
    lcm = 1
    for i in range(1, n+1):
        lcm = int((lcm*i)/gcd(lcm,i))
    return lcm

print(LCM(20))
