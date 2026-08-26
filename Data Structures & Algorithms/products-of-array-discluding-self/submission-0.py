class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        if len(nums) == 2:
            return [nums[1],nums[0]]

        n = len(nums)
        ans_one = [1] * n
        ans_two = [1] * n
        result = [1] * n
        
        prefix = nums[0]
        suffix = nums[n - 1]

        for i in range(n):
            if i == 0:
                ans_one[i] = prefix
                continue
            
            prefix = prefix * nums[i]
            ans_one[i] = prefix
    
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                ans_two[i] = suffix
                continue
            
            suffix = suffix * nums[i]
            ans_two[i] = suffix
            

        for i in range(n):
            
            if i == 0:
                result[i] = ans_two[i + 1]
                continue

            if i == n - 1:
                result[i] = ans_one[i - 1]
                continue

            result[i] = ans_one[i - 1] * ans_two[i + 1]

        return result



        