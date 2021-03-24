# Given a binary array, find the maximum number of consecutive 1s in this array.
def max_consecutive_ones(arr):
    count = 0
    max_count = 0
    for num in arr:
        if num == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    return max(max_count, count)


def one_liner_consecutive_ones(arr):
    return max(map(len, ''.join(map(str, arr)).split('0')))


if __name__ == "__main__":
    nums = list(map(int, input().split(',')))
    print('{0},{1}'.format(max_consecutive_ones(nums), one_liner_consecutive_ones(nums)))
