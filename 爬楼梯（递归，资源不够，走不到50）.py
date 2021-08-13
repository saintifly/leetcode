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
    global  path_1
    if n==0:
        return 0
    if n == 1:
        path_1 = 1
        return path_1
    if n == 2:
        path_1 = 2
        return path_1
    if n == 3:
        path_1 = 4
        return path_1
    if n>3:
        path_1 = 0
        path_1 = path_1+clim_path(n-1)+clim_path(n-2)+clim_path(n-3)
        return path_1

if __name__ == '__main__':
    ret = clim_path(30)
    print(ret)