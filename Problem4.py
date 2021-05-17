"""
A palindromic number reads the same both ways. 

The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def PalindromeChecker(num):
    temp = str(num)
    if temp == temp[::-1]:
        return True
    else:
        return False

three_dig_list = [x for x in range(100,1000)]
pali_arr = []
for num1 in x:
    for num2 in x:
        if PalindromeChecker(num1*num2) == True:
            pali_arr.append(num1*num2)
        
print(max(pali_arr))
