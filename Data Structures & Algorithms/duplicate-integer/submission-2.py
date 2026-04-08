class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valCount = {}
        for value in nums:
            if value in valCount:
                valCount[value] = valCount[value]+ 1
            else:
                valCount[value] = 1
        
        for value in nums:
            if valCount[value] > 1:
                return True
            
        return False