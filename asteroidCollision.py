class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        while(True):
                if List ==[]:
                    break
                dellist = []
                for i,item in enumerate(asteroids[:-1]):
                    if int(item)>0 and int(asteroids[i+1])<0:
                        crash_sum = item + asteroids[i+1]
                        if crash_sum >0:
                            dellist.append(i+1)
                        if crash_sum ==0:
                            dellist.append(i)
                            dellist.append(i+1)
                        if crash_sum <0:
                            dellist.append(i)
                count =0
                for i in dellist:
                    i = i -count
                    del asteroids[i]
                    count = count + 1
                flag = 0
                for i in asteroids:
                    if i>0 and flag==0:
                        flag =1
                        continue
                    if flag ==1 and i<0:
                        flag =2
                if flag < 2:
                    break
        return asteroids