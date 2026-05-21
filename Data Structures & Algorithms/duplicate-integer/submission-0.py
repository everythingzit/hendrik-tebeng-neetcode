class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeat_check = []
        for num in nums:
            if num in repeat_check:
                return True
            else:
                repeat_check.append(num)

        return False