class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valCount = {}
        for value in nums:
            if value in valCount:
                return True
            else:
                valCount[value] = 1
               
        return False