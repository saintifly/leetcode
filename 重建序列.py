class Solution:
    def findOrder(self, numCourses: int, dependcourseInfo,updenpend) -> List[int]:
        dependcourse = []
        start =[]
        ret  = []
        # for i in range(numCourses):
        #     if i not in dependcourse:
        #         if i not in dependcourseInfo:
        #             ret.append(i)
        #         else:
        #             start.append(i)
        for i in updenpend:
            if updenpend[i]==[]:
                start.append(i)
        count=0
        if start ==[]:
            return []
        ret=ret+ start
        next =[]
        other =[]
        if len(start)>1:
            return []
        while(start!=[] and count<=numCourses+3):
            for i in start:
                if i not in dependcourseInfo.keys():
                    other.append(i)
                    continue
                else:
                    if i not in ret:
                        ret.append(i)
                        if i in updenpend.keys():
                            del(updenpend[i])
                for k in dependcourseInfo[i]:
                    if i in updenpend[k]:
                        updenpend[k].remove(i)
                for j in dependcourseInfo[i]:
                    if updenpend[j] ==[]:
                        next.append(j)
            if len(next)>1:
                return []
            if next!=[]:
                start = [next[0]]
                next = next[1:]
            else:
                if start!=[] and start[0] not in dependcourseInfo.keys():
                    next.append(start[0])
                start=[]
            count = count +1
        if count>numCourses+1:
            return []
        for k in start+next+other:
            if k not in ret:
                ret.append(k)
        if len(ret) == numCourses:
            return ret
        else:
            return []

    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        dependcourseInfo={}
        updenpend = {}
        for i in seqs:
            for j in i:
                dependcourseInfo[j]=[]
                updenpend[j]=[]
        if len(updenpend)!=len(org):
            return False
        for i in seqs:
            for j,item in enumerate(i):
                if j < len(i)-1:
                    if item not in dependcourseInfo.keys():
                        dependcourseInfo[item] = [i[j+1]]
                    else:
                        if i[j+1] not in dependcourseInfo[item]:
                            dependcourseInfo[item].append(i[j+1])
                    if i[j+1] not in updenpend.keys():
                        updenpend[i[j+1]] = [item]
                    else:
                        if item not in updenpend[i[j + 1]]:
                            updenpend[i[j + 1]].append(item)
        ret = self.findOrder(len(org),dependcourseInfo,updenpend)
        if ret  == org:
            return True
        else:
            return False