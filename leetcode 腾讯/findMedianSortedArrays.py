class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num3=nums1+nums2
        num3.sort()
        len_num = len(num3)
        len_half = len_num/2
        if len_num==2:
            halft_ret = float(num3[0]+num3[1])/2
        elif len_num==1:
            halft_ret = float(num3[0]) 
        elif len_num==0:
            return 0
        else:
            if len_num%2==0:
                print len_half
                halft_ret = float(num3[len_half-1]+num3[len_half])/2
            else:
                halft_ret =  float(num3[len_half])
        return halft_ret
        