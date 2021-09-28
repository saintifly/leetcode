class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        print(1111111,self.cache)
        if key in self.cache:
            tmp = self.cache[key]
            del self.cache[key]
            self.cache[key] = tmp
            return self.cache[key]
        else:
            return -1



    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        print(self.cache.keys(),self.cache)
        if len(self.cache) == self.capacity:
            if key in self.cache:
                del self.cache[key]
            else:
                del_used = list(self.cache.keys())
                del self.cache[del_used[0]]
            self.cache[key] = value
        else:
            self.cache[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)