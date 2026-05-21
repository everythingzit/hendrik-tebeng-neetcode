class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []

        num_frequencies = defaultdict(int)
        for num in nums:
            num_frequencies[num] += 1

        while k > 0:
            max = 0
            max_num = -1
            for num in num_frequencies:
                if num_frequencies[num] > max:
                    max = num_frequencies[num]
                    max_num = num

            output.append(max_num)
            num_frequencies.pop(max_num)
            k -= 1

        return output
        