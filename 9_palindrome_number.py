"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
"""


def isPalindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False


def test():
    nums = [121, -121, 10, 1234567890, 12121212121]
    for num in nums:
        result = isPalindrome(num)
        print(f'{str(num).ljust(12)} {result}')


test()
