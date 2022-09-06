from typing import List


def find_target_sum_ways(nums: list[int], target: int) -> int:
    """
    We're trying to find the number of ways to get to the target
    sum by adding or subtracting the numbers in the array.

    We can do this by recursively calling the function on the next
    number in the array, and adding or subtracting that number
    from the current sum.

    We can use memoization to speed up the function.

    We can also use a bottom-up approach to solve this problem.

    Here's the bottom-up approach:

    :param nums: [1, 1, 1, 1, 1]
    :type nums: list[int]
    :param target: the target sum we're looking for
    :type target: int
    :return: The number of ways to reach the target sum.

     >>> find_target_sum_ways([1,1,1,1,1], 3)
     5
     >>> find_target_sum_ways([1], 1)
     1
    """

    dp = {}  # (index, total) -> # of ways

    def backtrack(i, total):
        if i == len(nums):
            return 1 if total == target else 0
        if (i, total) in dp:
            return dp[(i, total)]

        dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
            i + 1, total - nums[i]
        )
        return dp[(i, total)]

    return backtrack(0, 0)


def test_find_target_sum_ways():
    """
    >>> test_find_target_sum_ways()
    """
    assert 5 == find_target_sum_ways([1, 1, 1, 1, 1], 3)
    assert 1 == find_target_sum_ways([1], 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
