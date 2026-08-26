class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        
        seen = set()
        
        for i in range(0,len(nums)):
            if nums[i] in seen:
                return True
            
            seen.add(nums[i])
        

        return False
        