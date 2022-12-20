class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        #
        adj = [[] for i in range(n)]

        #
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # set to keep track of visited
        visit = set()

        # temp variable
        q = [source]

        # adding starting point to visited
        visit.add(source)

        # while q is not empty
        while q != []:

            # giving node the first item in q
            node = q.pop(0)

            # if our starting point is same as destination, return true
            if node == destination:
                return True

            for i in adj[node]:
                if i not in visit:
                    q.append(i)
                    visit.add(i)
        return False