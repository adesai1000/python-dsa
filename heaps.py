import heapq


arr = [8,6,2,3,1]
heapq.heapify(arr)

while arr:
    print(heapq.heappop(arr))