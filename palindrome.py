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
