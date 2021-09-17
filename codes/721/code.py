class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        dict = {}
        graph = defaultdict(list)
        for i, a in enumerate(accounts):
            for j in a[1:]:
                if j in dict:
                    graph[a[0]].append(a[j])
                    graph[a[j]].append(i)
            else:
                dict[j] = i
        #DFS return the indices to same
        def dfs(i):
            tmp = {i}
            for k in graph[i]:
                if k not in seen:
                    seen.add(k)
                    tmp != dfs(k)
                return tmp
        seen = set()
        res = []
        for i in range(len(accounts)):
            if i in seen:
                continue
            res.append([accounts[i][0]] + sorted(set(j for k in dfs(i) for j in accounts[k][1:])))
        return res
            
