import heapq 
# Lecture#10; LeetCode#253
# type intervals: List[List[int]]
# rtype: int
def IntervalPartitioning(intervals):
    if not intervals: return 0

    rooms = []
    intervals.sort(key= lambda x: x[0])
    heapq.heappush(rooms, intervals[0][1])

    for i in intervals[1:]:
        if rooms[0] <= i[0]:
            heapq.heappop(rooms)
        heapq.heappush(rooms, i[1])
    return len(rooms)