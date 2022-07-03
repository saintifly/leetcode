
from typing import List

def trap(height: List[int]) -> int:
    ###接雨水###
    '''
    到数组中从下标 i 到最左端最高的条形块高度 \text{left\_max}left_max。
    找到数组中从下标 i 到最右端最高的条形块高度 \text{right\_max}right_max。
    扫描数组 \text{height}height 并更新答案：
    累加 \min(\text{max\_left}[i],\text{max\_right}[i]) - \text{height}[i]min(max_left[i],max_right[i])−height[i] 到 ansans 上
    :param height:
    :return:
    '''
    height_len = len(height)
    ans = 0
    for i in range(height_len):
        if height[0:i]!=[]:
            current_left_max = max(height[0:i])
        else:
            current_left_max = 0
        if height[i+1:] != []:
            current_right_max = max(height[i+1:])
        else:
            current_right_max = 0
        ans =  ans + max(min(current_left_max,current_right_max)-height[i],0)
    return ans




if __name__ == '__main__':
    '''
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    输出为6
    '''
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    ans  = trap(height)
    print(ans)