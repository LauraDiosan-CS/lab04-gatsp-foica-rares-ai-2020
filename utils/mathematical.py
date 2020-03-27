def permMultiply(permA, permB):
    """
    out: return the result of multipling the permutations
    pre: permA and permB have elements in [0, n]
    """
    return [permA[x] for x in permB]


def testPermMul():
    assert permMultiply([2, 1, 0], [0, 2, 1]) == [2, 0, 1]

if __name__ == '__main__':
    testPermMul()
