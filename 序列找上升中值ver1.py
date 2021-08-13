'''
上升中值点
思路是使用栈来存满足前面的值均小于当前值的值. 因需要前面的值都小于该值, 需要用一个max来存到目前为止的最大值, 若当前值大于max, 则满足第一个条件. 若后续出现更小的值, 则之前压入栈中的值一定不满足第二个条件, 因此应出栈.
一遍找符合前面都小于的数, 后一遍从后向前找符合后面都大于的数, 两次均存在的数即为目标值)
'''
import os

def get_up_point(input_list=[]):
    '''
    从列表中获取左边都是比它小的点，右边都是比它大的点
    :param input_list:
    :return:
    '''
    point_result_up = []
    point_result_down =[]
    input_list_sort = sorted(input_list)
    max_before = input_list[0]
    del_elemnt =[]
    for i in range(len(input_list)):
        if i==0:
            continue
        if input_list[i] > max_before:
            point_result_up.append(input_list[i])
            max_before = input_list[i]
    max_before = input_list[-1]
    for i in range(len(input_list)-1,0,-1):
        if i==0:
            continue
        if input_list[i] < max_before:
            point_result_down.append(input_list[i])
            max_before = input_list[i]
    point_result_up = [x for x in point_result_up if x in point_result_down]
    return point_result_up

if __name__ == '__main__':
    test_find_point = get_up_point([1,2,3,3,2,3,4,8,7])
    print(test_find_point)
