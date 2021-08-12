class Solution(object):
    return_tmp=''
    num_1 = 1
    phone_num_map_str = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno",\
                     "7":"pqrs","8":"tuv","9":"wxyz"}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        :param input_nums:
        :return:
        """
        if len(digits)==0:
            return []
        if self.num_1 == 1:
            self.return_tmp=''
            self.List=[]
            for i in digits:
                if str(i) =="7" or str(i) =='9':
                    self.num_1 = 4*self.num_1
                else:
                    self.num_1 = 3*self.num_1
        if len(digits) == 1:
            for i in self.phone_num_map_str[digits]:
                self.List.append(self.return_tmp+str(i))
            self.return_tmp = ''
            if len(self.List) ==self.num_1:
                return self.List
            return ''
        first_input_num = digits[0]
        for i in self.phone_num_map_str[first_input_num]:
            self.return_tmp = self.return_tmp + str(i)
            self.return_tmp = self.return_tmp + str((self.letterCombinations(str(digits[1:]))))
            self.return_tmp = self.return_tmp[:-1]
        self.return_tmp = self.return_tmp[:-1]
        if len(self.List) ==self.num_1:
            return self.List
        return ''