class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        chars = {}
        max_f = 0
        res = 0

        for r in range(len(s)):
            if s[r] in chars:
                chars[s[r]] += 1
            else:
                chars[s[r]] = 1
            
            max_f = max(max_f, chars[s[r]])

            while r -  l + 1 - max_f > k:
                chars[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res
        