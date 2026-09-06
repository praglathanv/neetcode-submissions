class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        l = 0
        min_len = None

        for r in range(len(nums)):

            sum += nums[r]

            if sum >= target:
                if not min_len:
                    min_len = r - l + 1
                else: 
                    min_len = min(r - l + 1, min_len)

                while sum >= target:
                    sum -= nums[l]
                    l += 1
                
                if sum == target:
                    min_len = min(r - l + 1, min_len)
                
                l -= 1
                sum += nums[l]
                min_len = min(r - l +1, min_len)
        
        if not min_len:
            return 0
        else:
            return min_len
        