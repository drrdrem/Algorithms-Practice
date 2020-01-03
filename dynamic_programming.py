import numpy as np

# Lecture#18
# type W: int; val: List[int]; wt: List[int]
# rtype: int
def knapsack(W, val, wt):
    N = len(val)
    M = [[0 for w in range(W+1)] for i in range(N+1)]
    
    for i in range(N+1):
        for w in range(W+1):
            if i==0 or w==0: M[i][w] = 0
            elif wt[i-1]<=W: M[i][w] = max(val[i-1]+M[i-1][w-wt[i-1]], M[i-1][w])
            else: M[i][w] = M[i-1][w]
                
    return M[N][W] 


# Lecture#19
# type nums: seq
# rtype: seq
# Codes modified from: http://cgoliver.com/2017/01/15/Nussinov.html
def isPair(tupple):
    if tupple in [('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')]: return True
    return False

def Opt(i, j, seq):
    if j-i<=4: return 0
    else:
        not_included = Opt(i, j-1, seq)
        includeds = [1 + Opt(i, t-1, seq) + Opt(t+1, j-1, seq) for t in range(i, j-4) if isPair((seq[t], seq[j]))]
        
        included = 0 if not includeds else max(includeds)
        
        return max(not_included, included)

def traceback(i, j, sec_stru, dp, seq):
    if j <= i:  return
    elif dp[i][j] == dp[i][j-1]:
        traceback(i, j-1, sec_stru, dp, seq)
    else:
        for l in [b for b in range(i, j-4) if isPair((seq[b], seq[j]))]:
            if l-1 < 0:
                if dp[i][j]==dp[l+1][j-1]+1:
                    sec_stru.append((l,j))
                    traceback(l+1, j-1, sec_stru, dp, seq)
                    break
            elif dp[i][j]==dp[i][l-1]+dp[l+1][j-1]+1:
                sec_stru.append((l,j))
                traceback(i, l-1, sec_stru, dp, seq)
                traceback(l+1, j-1, sec_stru, dp, seq)
                break
                    
def print_sec_struc(seq, sec_struc):
    res = ['.' for _ in range(len(seq))]
    for s in sec_struc:
        res[min(s)] = '('
        res[max(s)] = ')'
    return "".join(res)

def Nussinov(seq):
    N = len(seq)
    dp = np.empty((N, N))
    dp[:] = np.NAN
    sec_struc = []
    for l in range(0, 4):
        for i in range(N-l):
            j = i + l
            dp[i][j] = 0
    
    for l in range(4, N):
        for i in range(N-l):
            j = i + l
            dp[i][j] = Opt(i, j, seq)
            
    for i in range(N):
        for j in range(0, i):
            dp[i][j] = dp[j][i]
            
    traceback(0, N-1, sec_struc, dp, seq)
    return (seq, print_sec_struc(seq, sec_struc))


# Lecture#20; Leetcode#300
# type nums: List[int]
# rtype: int
def LIS(nums): 
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