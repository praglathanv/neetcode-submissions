import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        heap = []
        result = []

        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1


        for num,count in map.items():
            heapq.heappush(heap,[count,num])

            if len(heap) > k:
                heapq.heappop(heap)

        for el in heap:
            result.append(el[1])

        return result




        