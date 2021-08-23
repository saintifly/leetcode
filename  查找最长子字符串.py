import os
import sys
def getMaxSubStr(inptStr:str)->str:
    """
    求最大子字符串
    :param S:
    :return:
    """
    maxLen = 0
    str1 = ''
    max_str = ''
    for i in range(len(inptStr)):
        for item in inptStr[i:]:
            if item not in str1:
                str1 = str1+item
            else:
                temp = len(str1)
                if temp > maxLen:
                    maxLen = temp
                    max_str = str1
                    str1 = ''
                str1 = ''
        temp = len(str1)
        print(max_str)
        if temp > maxLen:
            maxLen = temp
            max_str = str1
            str1 = ''
        str1 =''
    return max_str

if __name__ == '__main__':
    ret = getMaxSubStr('jbpnbwwd')
    print(ret)
