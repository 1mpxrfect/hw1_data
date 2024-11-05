def intersection(nums1, nums2):
    elements = {}
    for num in nums1:
        elements[num] = True

    result = []

    for num in nums2:
        if num in elements and num not in result:
            result.append(num)

    return result
