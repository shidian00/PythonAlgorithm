def max_product_subarray(nums: list[int]) -> int:
    """
    The below code is finding the max product of a subarray of length k

    :param nums: list[int]
    :type nums: list[int]
    :return: The max product of a subarray of length k.

    >>> max_product_subarray([2,3,-2,4])
    6
    >>> max_product_subarray([-2,0,-1])
    0
    """

    N = len(nums)
    dp_max = [0] * N
    dp_min = [0] * N

    dp_max[0] = dp_min[0] = nums[0]

    # first pass, find min and max at each pointin the array
    for i in range(1, N):
        dp_max[i] = max(nums[i] * dp_max[i - 1], nums[i], dp_min[i - 1] * nums[i])
        dp_min[i] = min(nums[i] * dp_min[i - 1], nums[i], dp_max[i - 1] * nums[i])

    # second pass, find the max that could be obtained at each point using the two dp
    maxes = [0] * N
    # starting off take max of the beginning

    for i in range(N):
        maxes[i] = max(dp_max[i], dp_min[i])

    return max(maxes)


def test_max_product_subarray():
    """
    >>> test_max_product_subarray()
    """
    assert 6 == max_product_subarray([2, 3, -2, 4])
    assert 0 == max_product_subarray([-2, 0, -1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
