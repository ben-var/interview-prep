class Solution:
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # run DFS with alternating sets adding each node. if a node 
        # is tried to be added to a set in which
        # it already exists in, then return false
        #
        # otherwise, return true
        
        A, B = set(), set()
        
        inA = True
        for src, neighbors in enumerate(graph):
            print ('src, neigh', src, neighbors)
            if inA:
                if src in B:
                    return False
                A.add(src)
            else:
                if src in A:
                    return False
                B.add(src)
                
            inA = not inA
                    
            for tgt in neighbors:
                if inA:
                    if tgt in B:
                        return False
                    A.add(tgt)
                else:
                    if tgt in A:
                        return False
                    B.add(tgt)

        return True