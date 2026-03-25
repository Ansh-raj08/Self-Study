"""
LeetCode Problem 371: Sum of Two Integers

Given two integers a and b, return the sum of the two integers without using
operators '+' and '-'.
"""


def getSum(a: int, b: int) -> int:
    """
    Add two integers using bit manipulation.

    Idea:
    - XOR gives sum bits without carry.
    - AND + left shift gives carry bits.
    - Repeat until carry becomes 0.

    Python uses unbounded integers, so we simulate 32-bit behavior with masks.
    """
    mask = 0xFFFFFFFF        # 32 bits of 1s
    max_int = 0x7FFFFFFF     # Largest positive 32-bit integer

    while b != 0:
        carry = (a & b) & mask
        a = (a ^ b) & mask
        b = (carry << 1) & mask

    # Convert from 32-bit unsigned to signed integer.
    return a if a <= max_int else ~(a ^ mask)


if __name__ == "__main__":
    test_cases = [
        (1, 2),
        (2, 3),
        (-1, 1),
        (-2, -3),
        (123, 456),
    ]

    for x, y in test_cases:
        print(f"getSum({x}, {y}) = {getSum(x, y)}")
