class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from queue import PriorityQueue
        nums_len = len(nums)
        res_out = []
        TreeQueue = PriorityQueue()
        if nums_len<=k:
            res_out.append(max(nums))
            return res_out
        else:
            for i in range(k-1):
                TreeQueue.put((-nums[i], i))
        for i,num in enumerate(nums[k-1:]):
            TreeQueue.put((-num, i+k-1))
            if not TreeQueue.empty():
                Getout = TreeQueue.get()
                while Getout[1] <i:
                    if not TreeQueue.empty():
                        Getout = TreeQueue.get()
                    else:
                        break
                else:
                    TreeQueue.put(Getout)
                res_out.append(-Getout[0])
        return res_out