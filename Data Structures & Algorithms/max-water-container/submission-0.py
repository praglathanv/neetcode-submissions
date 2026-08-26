class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxfill = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            h = min(heights[left], heights[right])
            w = right - left
            fill = h * w

            if fill > maxfill:
                maxfill = fill

            if heights[left] == heights[right]:
                left += 1
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxfill
        