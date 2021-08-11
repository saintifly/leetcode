import os

#求给定n，求下一个回数n，即：数值从左到右，从右到左，内容是一致的。
def next_circle_n(input_n):
    '''
    :param input_n: 任意一个数input_n
    :return: circle_n:任意回数
    '''
    n_str =  str(input_n)
    n_num_len = len(n_str)
    if n_num_len<2:
        return input_n
    n_num_len_half_rem = n_num_len%2
    if n_num_len_half_rem == 0:
        output_n_str =  n_str[:n_num_len//2]+n_str[n_num_len//2-1::-1]
        if int(output_n_str)>=input_n:
            return int(output_n_str)
        else:
            output_n_str = n_str[:(n_num_len//2)-1] + str(int(n_str[n_num_len//2-1])+1)
            output_n_str = output_n_str +output_n_str[-1::-1]
            return int(output_n_str)
    else:
        output_n_str =  n_str[:n_num_len//2]+n_str[n_num_len//2]+n_str[n_num_len//2-1::-1]
        if int(output_n_str)>=input_n:
            return int(output_n_str)
        else:
            output_n_str = n_str[:n_num_len//2] + str(int(n_str[n_num_len//2])+1)+n_str[n_num_len//2-1::-1]
            return int(output_n_str)

if __name__ == '__main__':
    print(output_n)