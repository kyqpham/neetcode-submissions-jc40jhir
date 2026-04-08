class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        returned = False
        for value in nums:
            if nums.count(value) > 1:
                returned = True
        
        return returned