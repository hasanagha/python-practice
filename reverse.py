''' Method to reverse a string without using python's in build function '''


def reverse(x):
    is_negative = False

    if x < 0:
        is_negative = True
        x = -(x)

    ls = []
    while x != 0:
        ls = [str(x % 10)] + ls
        x = x // 10

    rev = int(''.join(ls[::-1]))

    if is_negative:
        return -(rev)

    return rev


if __name__ == '__main__':
    s = reverse('the world is heaven')
