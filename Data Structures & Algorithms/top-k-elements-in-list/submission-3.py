import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1

        freq_heap = [(-frequencies[num], num) for num in frequencies]
        heapq.heapify(freq_heap)

        output = []
        while k > 0:
            output.append(heapq.heappop(freq_heap)[1])
            k -= 1

        return output
