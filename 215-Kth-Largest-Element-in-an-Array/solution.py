class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        
        minHeap = []
        for num in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            elif minHeap[0] < num:
                heapq.heappushpop(minHeap, num)
        return minHeap[0]