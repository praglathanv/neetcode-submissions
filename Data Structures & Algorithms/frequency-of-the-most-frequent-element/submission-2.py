class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        g = 0
        l = 0
        max_w = 0
        w_c = 0

        for r in range(len(nums)):
            if nums[r] > g:
                g = nums[r]
            
            while g * (r - l) - w_c > k:
                w_c -= nums[l]
                l += 1
            
            w_c += nums[r]

            max_w = max(max_w, r - l + 1)
        
        return max_w