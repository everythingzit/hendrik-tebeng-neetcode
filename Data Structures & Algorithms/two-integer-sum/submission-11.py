class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums:
                indices.append(i)
                j = len(nums) - (1+ nums[::-1].index(diff))
                indices.append(j)

                if i != j:
                    break
                else:
                    indices = []
        
        return indices