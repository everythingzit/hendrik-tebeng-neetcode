from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked_nums = defaultdict(int)

        for index, num in enumerate(nums):
            diff = target - num
            if diff in checked_nums:
                return [checked_nums[diff], index]
            else:
                checked_nums[num] = index