class Solution:
    # UNFINISHED
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not prerequisites: return False
        
        prs = {}
        for pr in prerequisites:
            prs[pr[0]] = pr[1]
            
        def dfs(pos, pathlen, explored, target=numCourses):
            if pathlen >= target:
                return True
            elif pos in explored:
                return False
            
            return dfs(pos)
            
        for i in range(len(prerequisites)):
            if dfs(i, 1, set()):
                return True
        return False