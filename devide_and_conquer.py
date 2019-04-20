
# Lecture#13; LeetCode#None
# type a: float
# type b: float
# rtype: float
import numpy as np
def func(x): 
    return np.sin(x) - 100/np.sqrt(x) + x**4

# Recurssive Method
def bisection(a,b):
	if S
	if (b-a) <0.01:
		return a
	else:
		m = (a+b)/2
		if func(m)  == 0:
			return m
		elif func(m) <0:
			return bisection(m,b)
		else:
			return bisection(a,m)

# Iterative Method          
def bisection2(a,b): 
    m = a 
    while ((b-a) >= 0.01): 
        m = (a+b)/2
        if (func(m) == 0.0): 
            break
        if (func(m)*func(a) < 0): 
            b = m 
        else: 
            a = m 
    return c


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