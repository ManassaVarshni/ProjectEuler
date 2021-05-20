"""

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

def SumOfSquares1(start,end):
    return sum(i*i for i in range(start,end))

def SquareOfSums1(start,end):
    return (sum(i for i in range(start,end)))**2

difference = SquareOfSums1(1,101) - SumOfSquares1(1,101)
print(difference)
