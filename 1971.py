class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        q = [source]
        visit.add(source)
        while q != []:
            node = q.pop(0)
            if node == destination:
                return True

            for i in adj[node]:
                if i not in visit:
                    q.append(i)
                    visit.add(i)
        return False