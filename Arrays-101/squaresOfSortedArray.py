# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
# non-decreasing order.

def square_sorted_array(nums):
    return sorted([x * x for x in nums])


def square_sorted_array_two_pointers(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square * square
    return result


def square_sorted_array_deque(nums):
    from collections import deque
    result = deque()
    left, right = 0, len(nums) - 1
    for i in range(len(nums)):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result.appendleft(square * square)
    return list(result)


if __name__ == "__main__":
    arr = list(map(int, input().split(',')))
    print("{0}\n{1}\n{2}".format(square_sorted_array(arr), square_sorted_array_two_pointers(arr)
                                 , square_sorted_array_deque(arr)))
