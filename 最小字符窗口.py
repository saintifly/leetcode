class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tLen = len(t)
        sLen = len(s)
        count1 = tLen
        minLen = s
        minNum = sLen + 1
        if sLen < tLen:
            return ''
        thash = Counter(t)
        j = 0
        ans = ''
        for i in range(len(s)):
            if s[i] in thash:
                if thash[s[i]] > 0:
                    count1 = count1 - 1
                thash[s[i]] -= 1
            while count1 == 0:
                if i - j + 1 < minNum:
                    minNum = i - j + 1
                    ans = s[j:i + 1]
                if s[j] in thash:
                    if thash[s[j]] >= 0:
                        count1 += 1
                    thash[s[j]] += 1
                j += 1
        return ans
