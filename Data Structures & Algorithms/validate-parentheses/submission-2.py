class Solution:
    def isValid(self, s: str) -> bool:
        map_l = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }
        stack = []

        for i in range(len(s)):
            if s[i] in map_l:
                if len(stack) == 0:
                    return False

                if map_l[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        
        if len(stack) == 0:
            return True
        else:
            return False
        