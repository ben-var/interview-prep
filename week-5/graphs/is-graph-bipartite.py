class Solution:

    def isBipartite(self, graph: List[List[int]]) -> bool:

        colorings = {}

        def dfsColor(pos):
            for i in graph[pos]:
                if i in colorings:
                    if colorings[i] == colorings[pos]:
                        return False
                else:
                    colorings[i] = not colorings[pos]
                    if not dfsColor(i):
                        return False
            return True

        for i in range(len(graph)):
            if i not in colorings:
                colorings[i] = True
                if not dfsColor(i):
                    return False
        return True
