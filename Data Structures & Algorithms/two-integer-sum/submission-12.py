class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = -1
        j = -1
        first_num = 0

        for index, num in enumerate(nums):
            if i >= 0 and num + first_num == target:
                j = index
                break

            if (target - num) in set(nums[index + 1:]):
                i = index
                first_num = num
        
        return [i, j]
        
