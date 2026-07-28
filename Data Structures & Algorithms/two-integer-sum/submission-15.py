class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = defaultdict(int)

        for index, num in enumerate(nums):
            diff = target - num
            if diff in num_dict:
                return[num_dict[diff], index]
            
            num_dict[num] = index