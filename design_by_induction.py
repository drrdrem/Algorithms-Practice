
# Lecture#4; LeetCode#53
# type nums: List[int]
# rtype: int
 def maxSumSubsequence(nums):
    S=nums[0];U=0;
    for x in nums:
        if x>S:
            S = x
        if (x+U>S):
            S = x+U
        if (x+U>0):
            U = x+U
        else:
            U=0
    return S


# HW02P3; LeetCode#152
# The solution is wrong
# type nums: List[int]
# rtype: int
def maxProduct(nums):
    if len(nums)==1: return nums[0]
    
    ps = ns = 1; o = 0
    for i in range(len(nums)):
        if nums[i]==0: ps = ns = 1
        else: 
            ps, ns = max(ps*nums[i], ns*nums[i], nums[i]), min(ps*nums[i], ns*nums[i], nums[i])
            
            o = max(o, ps)          
    return o