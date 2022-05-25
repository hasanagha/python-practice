'''function to check if a string passed
   is palindrome or not

   Palindrome: A palindromic word is a word (such as radar) that remains the same when its reversed.'''


def isPalindrome(s):
    l = len(s)
    # Run loop from 0 to len/2
    for i in range(0, int(l / 2)):
        if str[i] != str[l - i - 1]:
            return False

    return True



def isPalindromeInBuild(s):
 
    # Using predefined function to
    # reverse to string print(s)
    rev = ''.join(reversed(s))
 
    # Checking if both string are
    # equal or not
    return s == rev



# function which return reverse of a string
def isPalindrome2(s):
    return s == s[::-1]


if __name__ == '__main__':
    s = 'level'
    isPalindrome(s)
