class LRUCache:

    def __init__(self, capacity: int):

        self.cache = {}
        self.capacity = capacity
        self.used =[]


    def get(self, key: int) -> int:
        if key in self.cache:
            if key not in self.used:
                self.used.append(key)
            else:
                self.used.remove(key)
                self.used.append(key)
            return self.cache[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if len(self.cache) >=self.capacity:
            if key in self.cache:
                self.cache[key] = value
                if key not in self.used:
                    self.used.append(key)
                else:
                    self.used.remove(key)
                    self.used.append(key)
                return
            flag = 0
            delkey = 0
            # for i in self.cache.keys():
            #     if i not in self.used:
            #         flag = 1
            #         delkey = i
            #         break
            # print(self.used)   
            # if flag == 0:
            #     print(1111,self.cache)
            #     print(22222,self.used)
            #     del self.cache[self.used[0]]
            # else:
            #     del self.cache[delkey]
            #     self.used[0].remove(key)
            print(1111,self.cache)
            print(22222,self.used)
            del self.cache[self.used[0]]
            self.used = self.used[1:]
            self.cache[key] = value
            if key not in self.used:
                self.used.append(key)
            else:
                self.used.remove(key)
                self.used.append(key)
            print('xxx',self.cache)
        else:
            self.cache[key] = value
            if key not in self.used:
                self.used.append(key)
            else:
                self.used.remove(key)
                self.used.append(key)

