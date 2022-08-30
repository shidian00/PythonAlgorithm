# reverse bits of a number
# function to reverse
def reverseBits(n) -> int:
    """
    Reverse the bit
    >>> reverseBits(11)
    13
    """
    rev = 0

    # traversing bits of 'n' from the right
    while n > 0:
        # bitwise left shift 'rev' by 1
        rev = rev << 1
        # if current bit is '1'
        if n & 1 == 1:
            rev = rev ^ 1
        # bitwise right shift 'n' by 1
        n = n >> 1
    return rev


if __name__ == "__main__":
    from doctest import testmod

    testmod()
