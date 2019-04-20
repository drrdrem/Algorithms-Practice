# HW05P4; LeetCode#4
# type nums1: List[int]
# type nums2: List[int]
# rtype: float
def kSmallestValue(nums1, nums2, k):
    m ,n = len(nums1), len(nums2)
    if k > m + n: return
    
    if not nums1:
        return nums2[k]
    if not nums2:
        return nums1[k]

    if m//2 + n//2 >= k:
        if nums1[m//2]>nums2[n//2]:
            return kSmallestValue(nums1[:m//2], nums2, k)
        else: 
            return kSmallestValue(nums1, nums2[:n//2], k)
    else: 
        if nums1[m//2]>nums2[n//2]:
            return kSmallestValue(nums1, nums2[n//2+1:], k-n//2-1)
        else: 
            return kSmallestValue(nums1[m//2+1:], nums2, k-m//2-1)
            
def findMedianSortedArrays(nums1, nums2):
    l = len(nums1) + len(nums2)
    if l % 2 != 0:
        return kSmallestValue(nums1, nums2, l // 2)
    else:
        return (kSmallestValue(nums1, nums2, l // 2) + kSmallestValue(nums1, nums2, l // 2 - 1)) / 2.  