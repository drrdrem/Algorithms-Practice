
# Lecture#20; Leetcode#300
# type nums: List[int]
# rtype: int
def lengthOfLIS(nums): 
    if len(nums)==0: return 0
    dp = [1]
    for i in range(1, len(nums)):
        m = 0
        for j in range(0, i):
            if nums[j]<nums[i]:
                if m<dp[j]:
                    m =  dp[j]
        dp.append(1+m)             
    return max(dp)


# HW07P1; LeetCode#322
# type coins: List[int]
# type amount: int
# rtype: int
def Change(coins, amount):
    dp = [0]
    for i in range(1, amount+1):
        dp.append(float('inf'))
        for j in range(len(coins)):
            if i-coins[j]<0: continue
            dp[i] = min(1+dp[i-coins[j]], dp[i])
    return dp[-1] if dp[-1] != float('inf') else -1


# HW07P2; LeetCode#22
# type n: int
# rtype: List[str]
def BBS(n):
    dp = [[] for i in range(n + 1)]
    dp[0].append('')
    for k in range(n + 1):
        for i in range(k):
            dp[k] += ['(' + x + ')' + y for x in dp[i] for y in dp[k - i - 1]]
    return dp[n]