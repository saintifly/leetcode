class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        generate_ret = []
        ret_oneline = []
        for i in range(1,numRows+1):
            if i ==1:
                generate_ret.append([1])
                continue
            if i==2:
                generate_ret.append([1,1])
                continue
            ret_oneline = [1]*i
            for j in range(1,i-1):
                ret_oneline[j] = generate_ret[i-2][j]+generate_ret[i-2][j-i]
            generate_ret.append(ret_oneline)
        return generate_ret