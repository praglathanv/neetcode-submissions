class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        c= {}

        for r in range(len(nums)):
            if nums[r] in c:
                if abs(c[nums[r]] - r) <= k:
                    return True
                else:
                    c[nums[r]] = r
            else:
                c[nums[r]] = r
        
        return False
            
        