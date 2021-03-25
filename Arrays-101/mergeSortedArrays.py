# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a
# size equal to m + n such that it has enough space to hold additional elements from nums2.
def merge_sorted_array(nums1, nums2, m, n):
    # Write the elements of num2 into the end of nums1.
    for i in range(n):
        nums1[i + m] = nums2[i]

    # Sort nums1 list in-place.
    nums1.sort()
# Time Complexity : O((n+m)log(n+m)) built in tim sort used
# Space Complexity : O(n) can vary based on language


def merge_sorted_array_three_pointers(nums1, nums2, m, n):
    nums1_copy = nums1[:m]
    p1, p2, p = 0, 0, 0
    for p in range(n + m):
        if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
            nums1_copy[p1] = nums1[p]
            p1 += 1
        else:
            nums1[p]= nums2[p2]
            p2 += 1
# Time Complexity : O(n + m)  we did n + 2.m reads and n + 2.m writes
# SPace Complexity : O(m)


def merge_sorted_array_three_pointers_end(nums1, nums2, m, n):
        p1 = m - 1
        p2 = n - 1
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
# Time Complexity : O(n + m)
# SPace Complexity : O(1)

# Whenever you're trying to solve an array problem in-place, always consider the possibility of iterating backwards
# instead of forwards through the array. It can completely change the problem, and make it a lot easier.


if __name__ == "__main__":
    arr1 = list(map(int, input().split(',')))
    arr2 = list(map(int, input().split(',')))
    size1 = int(input())
    size2 = int(input())
    merge_sorted_array(arr1, arr2, size1, size2)
    print(arr1)
