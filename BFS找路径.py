import os
from typing import List

def get_into_allroom(rooms:List)->bool:
    num_level = [0]
    visitedroom= set(num_level)
    while (num_level):
            i = num_level.pop()
            print(visitedroom)
            for j in rooms[i]:
                if j not in visitedroom:
                    visitedroom.add(j)
                    num_level.append(j)
                    if len(visitedroom)==len(rooms): return True
    if len(visitedroom)==len(rooms):
        return True
    else:
        return False

if __name__ == '__main__':
    ret = get_into_allroom([[1],[2],[3],[]])
    print(ret)




