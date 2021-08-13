'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
'''

import os

def clim_path(n):
    '''
    爬楼梯方法：F(n)=F(n-1)+F(n)
    :param n:
    :return:
    '''
    path_1=[0]*n
    if n==0:
        return 0
    if n == 1:
        path_1[0] = 1
        return  path_1[0]
    if n == 2:
        path_1[1] = 2
        return  path_1[1]
    if n == 3:
        path_1[2] = 4
        return  path_1[2]
    path_1[0] = 1
    path_1[1] = 2
    path_1[2] = 4
    for i in range(3,n):
        path_1[i] = path_1[i-1] +path_1[i-2] +path_1[i-3]
    return path_1[n-1]
if __name__ == '__main__':
    ret = clim_path(100)
    print(ret)