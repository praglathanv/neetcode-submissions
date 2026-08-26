class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            if len(nums) == 0:
                return 0

            if len(nums) == 1:
                return 1
            
            nums.sort()
            maxlen = 0
            length = 0

            for i in range(len(nums)):
                if i == 0:
                    length += 1
                    maxlen = max(maxlen, length)
                    continue

                if nums[i] == nums[i - 1] + 1:
                    if length == 0:
                        length += 1

                    length += 1
                elif nums[i] == nums[i - 1]:
                    continue
                else:
                    maxlen = max(length, maxlen)
                    length = 0

                maxlen = max(length, maxlen)

            return maxlen  