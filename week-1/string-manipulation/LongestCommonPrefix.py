class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:        
        if len(strs) < 1:
            return ""
        
        # first word is assumed as the longest prefix until comparisons to the other strings
        lcp = strs[0]
                
        for i in range(1,len(strs)):
            compare = strs[i]
    
            # compare current longest common prefix with each subsequent string
            for j in range(len(lcp)):
                if j >= len(compare) or lcp[j] != compare[j]:
                    lcp = lcp[:j]
                    break    
        return lcp