# Given an array nums of integers, return how many of them contain an even number of digits.
# Constraints:

# 1 <= nums.length <= 500
# 1 <= nums[i] <= 10^5

def find_even_digit_nums(nums):
    even_digit_nums = 0
    for num in nums:
        c = 0
        while (num):
            num //= 10
            c += 1
        if not c % 2:
            even_digit_nums += 1
    return even_digit_nums
# Time complexity : O(n * k)
# Space Complexity : O(1)


def find_even_digit_using_log10(nums):
    from math import log10
    return sum(int(log10(num)) % 2 for num in nums)  # log10 + 1 is the number of digits
# Time complexity : O(n)
# Space Complexity : O(1)


def find_even_digits_using_logical_operators(nums):
    return sum(~ len(str(num))& 1 for num in nums) # ~x = (-x) - 1
# Time complexity : O(n)
# Space Complexity : O(1)


if __name__ == "__main__":
    arr = list(map(int, input().split(',')))
    print('{0}\n{1}\n{2}'.format(find_even_digit_nums(arr), find_even_digit_using_log10(arr),
                                 find_even_digits_using_logical_operators(arr)))

