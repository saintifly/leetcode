"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False
        for i in s:
            if i in t:
                t=t.replace(i,'',1)
            else:
                return False
        if t=='':
            return True
        else:
            return False

'''
重点的是字符的replace，可以带第三个参数替换的个数。
需要重新赋值给自己：t=t.replace(i,'',1)
'''