
''' Write a function that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
    For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

    Given A = [1, 2, 3], the function should return 4.
    Given A = [−1, −3], the function should return 1.

    Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].
'''


def solution(A):
    if len(A) > 100000:
        raise ValueError("range exceeded")

    # efficint way
    arr = set(A)

    for i in range(1, 1_000_002):
        if i not in arr:
            return i

    # an inefficient way
    # positive_int = [i for i in A if i > 0]
    # if not len(positive_int):
    #     return 1

    # m = min(positive_int)
    # x = max(positive_int)

    # for _ in range(m, x):
    #     if _ not in positive_int:
    #         return _

    return x + 1
