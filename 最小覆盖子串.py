def minWindow( s: str, t: str) -> str:
    ''''
    双指针
    '''
    left_p = 0
    right_p = 0
    m = len(s)
    n = len(t)
    result = ''
    target_str = {}
    for i in range(n):
        if t[i] in target_str:
            target_str[t[i]] += 1
        else:
            target_str[t[i]] = 1
    for i in range(m):
        right_p += 1
        if s[i] in target_str:
            target_str[s[i]] -= 1
            for j in range(n):
                if target_str[t[j]] > 0:
                    break
            if j == n - 1 and target_str[t[n - 1]] <= 0:
                temp = s[left_p:right_p]
                if result == '':
                    result = temp
                for k in range(left_p, right_p - n):
                    if s[k] in target_str:
                        target_str[s[k]] += 1
                        if target_str[s[k]] <= 0:
                            left_p += 1
                            temp = s[left_p:right_p]
                        else:
                            left_p += 1
                            break
                    else:
                        left_p = left_p + 1
                        temp = s[left_p:right_p]
                if len(temp)<len(result):
                    result = temp
    return result

if __name__ == '__main__':
    s = "cabwefgewcwaefgcf"
    t = "cae"
    out =  minWindow(s,t)
    print(out)
