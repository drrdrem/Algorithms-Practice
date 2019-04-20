
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


# HW02P2; LeetCode#53
# This is wrong
# type nums: List[int]
# rtype: int
def maxSumSubsequence2(nums):
    Sum = largest = smallest = 0
    for i in range(len(nums)):
        Sum = nums[i] + Sum                     # sum[i]
        smallest = min(smallest, Sum)           # min{0<=j<=i} sum[j]
        largest = max(largest, Sum-smallest)    # max{k<=i} sum[k] - min{0<=j<=k} sum[j]
    return largest

# Similar Approach but correct
def maxSumSubsequence3(nums):
    Sum = res = nums[0]
    for num in nums[1:]:
        Sum = max(num, Sum + num)
        res = max(res, Sum)
    return res


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