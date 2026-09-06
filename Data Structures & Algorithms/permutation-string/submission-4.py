class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            chars = Counter(s1)
            map = {}
            w = 0

            l = -1

            for r in range(len(s2)):
                if l == -1 and s2[r] in chars:
                    l = r

                if s2[r] in chars:
                    if chars[s2[r]] > 0:
                        chars[s2[r]] -= 1

                        if s2[r] in map:
                            map[s2[r]] += 1
                        else:
                            map[s2[r]] = 1

                        w += 1
                    else:
                        while s2[l] != s2[r]:
                            if s2[l] in chars:
                                chars[s2[l]] += 1
                                map[s2[l]] -= 1
                                w -= 1
                            l += 1

                        if chars[s2[r]] == 0:
                            l += 1
                else:
                    w = 0
                    l = r + 1
                    map = {}
                    chars = Counter(s1)
                if len(s1) == w:
                    #print(chars,map,w,r)
                    return True

            return False
        