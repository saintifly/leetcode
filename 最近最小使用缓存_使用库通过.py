from collections import OrderedDict as OD
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.od = OD()
        self.capacity = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.od:
            self.od.move_to_end(key)
        return self.od.get(key, -1)



    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.od:
            del self.od[key]
        self.od[key] = value
        if len(self.od) > self.capacity:
            self.od.popitem(last = False)