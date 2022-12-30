from collections import defaultdict
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q =[[0]]
        target= len(graph) -1
        res = []
        while q:
            temp = q.pop(0)
            if temp[-1] == target:
                res.append(temp)
            for nei in graph[temp[-1]]:
                q.append( temp +[nei])
        return res