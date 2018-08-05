# Find the Kth smallest element of two lists.

# Binary search
# Each time drop half of one array

# kth is '0' based.
def kth(nums1, nums2, k):

    if not nums1:
        return nums2[k]
    elif not nums2:
        return nums1[k]

    m1 = int(len(nums1) / 2)
    m2 = int(len(nums2) / 2)

    if m1 + m2 < k:
        if nums1[m1] < nums2[m2]:
            return kth(nums1[m1 + 1:], nums2, k - m1 - 1)
        else:
            return kth(nums1, nums2[m2 + 1:], k - m2 - 1)
    else:
        if nums1[m1] < nums2[m2]:
            return kth(nums1, nums2[:m2], k)
        else:
            return kth(nums1[:m1], nums2, k)

print(kth([1,3,5,7], [2,4,6,8], 1))
