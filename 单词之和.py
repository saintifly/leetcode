class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.out = {}
        self.words = {}


    def insert(self, key: str, val: int) -> None:
        if key not in self.words:
            self.words[key] = val
        else:
            for i,item in enumerate(key):
                self.out[key[:i+1]] = self.out[key[:i+1]] - self.words[key]
            self.words[key] = val
        for i,item in enumerate(key):
            if key[0:i+1] not in self.out:
                self.out[key[:i+1]] = val
                continue
            else:
                self.out[key[:i+1]] = self.out[key[:i+1]] + val
        print(self.out)



    def sum(self, prefix: str) -> int:
        if prefix in self.out.keys():
            return self.out[prefix]
        else:
            return 0



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)