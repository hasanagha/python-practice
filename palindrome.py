# Python program to check
# if a number passed is palindrome
# or not
# Palindrome: A palindromic number is a number (such as 16461) that remains the same when its digits are reversed

def isPalindrome(num):
    if num < 0:
        return False

    ls = []

    while num != 0:
        ls = [str(num % 10)] + ls
        num = num // 10

    return ls == ls[::-1]


if __name__ == '__main__':
    num = 121
    isPalindrome(num)
