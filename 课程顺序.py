class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites==[]:
            return [x for x in range(numCourses)]
        dependcourse = []
        dependcourseInfo = {}
        updenpend ={}
        for i in prerequisites:
            dependcourse.append(i[0])
            if i[0] not in updenpend.keys():
                updenpend[i[0]] =[i[1]]
            else:
                updenpend[i[0]].append(i[1])
            if i[1] not in dependcourseInfo.keys():
                dependcourseInfo[i[1]] =[i[0]]
            else:
                dependcourseInfo[i[1]].append(i[0])
        start =[]
        ret  = []
        for i in range(numCourses):
            if i not in dependcourse:
                if i not in dependcourseInfo:
                    ret.append(i)
                else:
                    start.append(i)
        count=0
        if start ==[]:
            return []
        ret=ret+ start
        next =[]
        other =[]
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
                    updenpend[k].remove(i)
                for j in dependcourseInfo[i]:
                    if updenpend[j] ==[]:
                        next.append(j) 
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
        if len(set(ret)) == numCourses:
            return ret
        else:
            return []