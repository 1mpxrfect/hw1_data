from typing import List


def findLengthOfLCIS(nums: List[int]) -> int:
    max_l = 1
    l = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            l += 1
            max_l = max(max_l, l)
        else:
            l = 1

    return max_l

if __name__ == '__main__':
    print(findLengthOfLCIS([1, 3, 5, 3, 2]))