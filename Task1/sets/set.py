from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    print(intersection([1, 2], [4, 3, 2, 1]))