class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))

            if key not in result:
                result[key] = []
            
            result[key].append(strs[i])
        
        return list(result.values())