
from typing import List
def countBits(n: int) -> List[int]:
    out = [0]
    k=1
    for i in range(1,n+1):
        if i&(i-1)==0:
            k=i
        out.append(out[i-k]+1)
    return out

if __name__ == '__main__':
    print(1111)
    print(countBits(2))