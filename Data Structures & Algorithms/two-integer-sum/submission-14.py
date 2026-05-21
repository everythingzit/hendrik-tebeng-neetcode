class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = -1
        j = -1

        num_hash = {}
        for index, num in enumerate(nums):
            if num in num_hash and num * 2 == target:
                return [num_hash[num], index]
            num_hash[num] = index

        for num in num_hash:
            sub = target - num
            if sub in num_hash and num_hash[num] != num_hash[sub]:
                return [num_hash[num], num_hash[sub]]

