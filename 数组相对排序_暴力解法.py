class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        map1 = list(zip(arr2,sorted(arr2)))
        map2 = list(zip(sorted(arr2),arr2))
        print(map1)
        tmp =[]
        for i,item in enumerate(arr1):
            for j in map1:
                if item ==j[0]:
                    arr1[i]=j[1]
                    break
            else:
                tmp.append(item)
        print(tmp)
        for i in tmp:
            arr1.remove(i)
        arr1 = sorted(arr1)
        print(arr1)
        for i,item in enumerate(arr1):
            for j in map2:
                if item ==j[0]:
                     arr1[i]=j[1]
        print(arr1)
        return arr1+sorted(tmp)