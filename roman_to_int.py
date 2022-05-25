''' function to convert roman numbers into digits
    for example: V  => 5
                 VI => 6
                 X  => 10 '''

roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def romanToInt(rs):
    """
    :type s: str
    :rtype: int
    """
    # Length of the given string
    sl = len(rs)

    # This variable will store result
    num = roman_dict[rs[sl - 1]]
    # Loop for each character from right to left
    for i in range(sl - 2, -1, -1):
        # Check if the character at right of current character is bigger or smaller
        val = roman_dict.get(rs[i], 0)

        if val >= roman_dict.get(rs[i + 1], 0):
            num += val
        else:
            num -= val

    return num


if __name__ == '__main__':
    print(romanToInt('IIIK'))
