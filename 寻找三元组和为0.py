'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a ，b ，c ，使得 a + b + c = 0 ？请找出所有和为 0 且 不重复 的三元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/1fGaJU
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
def threeSum( nums: List[int]) -> List[List[int]]:
    '''
    遍历找出a+b=-c
    :param nums:
    :return:
    '''
    nums = sorted(nums)
    num = len(nums)
    if num < 3:
        return []
    retsult = []
    for i in range(num-2):
        for j in range(i+1,num-2):
                if nums[j]==nums[j-1]:
                    continue
                if -(nums[i]+nums[j]) in nums[j+1:]:z
                        retsult.append([nums[i],nums[j],-(nums[i]+nums[j])])
    return retsult

if __name__ == '__main__':
    ret = threeSum([-1,0,1,2,-1,-4])
    print(ret)