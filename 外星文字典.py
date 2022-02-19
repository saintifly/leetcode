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
        # ret=ret+ start
        next =[]
        other =[]
        while(start!=[] and count<=numCourses+3):
            for i in start:
                if i not in dependcourseInfo.keys():
                    print('00000')
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

    def alienOrder(self, words: List[str]) -> str:
        wordsset = {}
        wordssetup ={}
        for i in words:
            for j in i:
                wordsset[j]=[]
                wordssetup[j]=[]
        n = len(words)
        for i,wordIterm in enumerate(words):
            if i<n-1:
                wordnext = words[i+1]
                m1 = len(wordIterm)
                m2 = len(wordnext)
                for j in range(min(m1,m2)):
                    if wordnext[j]== wordIterm[j]:
                        continue
                    else:
                        if wordnext[j] not in wordsset[wordIterm[j]]:
                            wordsset[wordIterm[j]].append(wordnext[j])
                            wordssetup[wordnext[j]].append(wordIterm[j])
                        break
                else:
                    if m1>m2:
                        return ''
        ret = self.findOrder(len(wordsset),wordsset,wordssetup)
        return ''.join(ret)