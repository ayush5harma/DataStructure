# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to
# the right.
# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place, do not return anything from your function.


def duplicate_zeroes(nums):
    n = len(nums) - 1
    zeroes = 0
    for i in range(n + 1):
        # dropping off number out of range
        if i > n - zeroes:
            break
        # counting zeroes on the way
        if nums[i] == 0:
            # if the last element in the permitted range is zero won't count it in duplicates
            if i == n - zeroes:
                # move this zero to the last permissible index and decrement the permissible index
                nums[n] = 0
                n -= 1
                break
            zeroes += 1
    last = n - zeroes
    for i in range(last, -1, -1):
        if nums[i] == 0:
            nums[i + zeroes] = 0
            zeroes -= 1
            nums[i + zeroes] = 0
        else:
            nums[i + zeroes] = nums[i]


# Time Complexity : O(n) two pass
# Space Complexity : O(1)


def duplicate_zeroes_in_place(nums):
    zeroes = nums.count(0)
    n = len(nums)
    for i in range(n - 1, -1, -1):
        if i + zeroes < n:
            nums[i + zeroes] = nums[i]  # this trims of numbers from the end which are out of permissible range
        if nums[i] == 0:  # check if the number added is zero, if so then add another zero
            zeroes -= 1
            if i + zeroes < n:
                nums[i + zeroes] = 0


if __name__ == "__main__":
    arr = list(map(int, input().split(',')))
    # duplicate_zeroes(arr)
    duplicate_zeroes_in_place(arr)
    print(arr)
