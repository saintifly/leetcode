class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        flag_start = 0
        sign = 1
        number = ''
        for char_c in str:
            if char_c.isdigit() and flag_start == 0:
                number = number + char_c
                flag_start = 1
                continue
            if char_c == "-" and flag_start == 0:
				sign = -1
				flag_start = 1;
				continue
            if char_c == "+" and flag_start == 0:
				sign = 1
				flag_start = 1;
				continue
            if char_c.isdigit() and flag_start == 1:
                number = number + char_c
                continue			
            if char_c.isdigit() is not True  and char_c !="-" and flag_start == 0:
                number = '0'
                break		
            if char_c.isdigit() is not True  and flag_start == 1:
                break		
                
        try:
            if str=="" or str=="-" or str=="+" or number=='':
                return 0
            if(len(number.lstrip('0'))>10 and sign==1 ) or (long(number)>pow(2,31)-1 and sign==1):
                return  pow(2,31)-1
            if(len(number.lstrip('0'))>10 and sign==-1 ) or (long(number)>pow(2,31) and sign==-1):
                return -1*pow(2,31) 
            return sign*int(number)
        except:
            return sys.maxint 