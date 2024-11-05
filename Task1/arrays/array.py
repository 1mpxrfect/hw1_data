from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1[m:] = nums2
    nums1.sort()


if __name__ == "__main__":
    print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))