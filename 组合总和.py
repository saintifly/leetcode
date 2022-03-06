class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        size = len(candidates)
        res = []

        def dfs(candidates, begin, path, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                dfs(candidates, index, path + [candidates[index]], target - candidates[index])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        dfs(candidates, 0, path, target)
        return res