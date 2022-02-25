class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums_init = nums
        
        
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums_init


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        self.num_ret = copy.deepcopy(self.nums_init)
        random.shuffle(self.num_ret) 
        return self.num_ret



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()