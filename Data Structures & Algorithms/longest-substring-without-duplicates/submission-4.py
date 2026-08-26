class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        w_s = 0
        length = 0
        maxlen = 0
        len_updated = False


        for i in range(len(s)):
            #print(s[i], w_s, i,"s e start")
            if s[i] in chars:
                if chars[s[i]] >= w_s:
                    length = i - w_s
                    #print(s[i], w_s, i,"s e reapeat", length)
                    maxlen = max(length, maxlen)
                    w_s = chars[s[i]] + 1
                    len_updated = True

            chars[s[i]] = i
            if not len_updated:
                length = i - w_s + 1
            len_updated = False
            #print(s[i], w_s, i,"s e end",length)
            maxlen = max(length, maxlen)

        return maxlen