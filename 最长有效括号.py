class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        子问题明确后，转移方程直接由子问题得到：
if s[i] == '(' :
    dp[i] = 0
if s[i] == ')' :
    if s[i - 1] == '(' :
        dp[i] = dp[i - 2] + 2 #要保证i - 2 >= 0

    if s[i - 1] == ')' and s[i - dp[i - 1] - 1] == '(' :
        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2 #要保证i - dp[i - 1] - 2 >= 0
初始条件和边界情况：
初始条件： dp[i] = 0 dp[i]=0

边界情况：需要保证计算过程中：i - 2 >= 0i−2>=0 和 i - dp[i - 1] - 2 >= 0i−dp[i−1]−2>=0

计算顺序：
无论第一个字符是什么，都有：dp[0] = 0dp[0]=0

然后依次计算：dp[1], dp[2], ..., dp[n - 1]dp[1],dp[2],...,dp[n−1]

结果是： max(dp[i])

作者：zhanganan0425
链接：https://leetcode-cn.com/problems/longest-valid-parentheses/solution/dong-tai-gui-hua-si-lu-xiang-jie-c-by-zhanganan042/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
 """
        sLen = len(s)
        if sLen <2:
            return 0 
        dp = [0]*sLen
        dp[0] = 0
        for i in range(1,sLen):
            if s[i] == '(' :
                dp[i] = 0
            if s[i] == ')' :
                if s[i - 1] == '(' :
                    if i-2>=0:
                        dp[i] = dp[i - 2] + 2 #要保证i - 2 >= 0
                    else:
                        dp[i] = 2
                if i - dp[i - 1] - 1>=0:
                    if s[i - 1] == ')' and s[i - dp[i - 1] - 1] == '(' :
                        if i - dp[i - 1] - 2>=0:
                            dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2 #要保证i - dp[i - 1] - 2 >= 0
                        else:
                            dp[i] = dp[i - 1]  + 2
                else:
                    dp[i] = 0

        return max(dp)