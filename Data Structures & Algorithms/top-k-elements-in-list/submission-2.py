import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs_dict = defaultdict(int)
        for num in nums:
            freqs_dict[num] += 1

        freqs_list = [(-freqs_dict[num], num) for num in freqs_dict]
        heapq.heapify(freqs_list)

        output = []
        while k > 0:
            next_val = heapq.heappop(freqs_list)[1]
            output.append(next_val)
            k -= 1
        
        return output
        