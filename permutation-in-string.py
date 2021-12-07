# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2) 
        if m>n: return False

        target_sign = [0] * (ord('z')-ord('a')+1)
        for i in range(m): target_sign[ord(s1[i])-ord('a')] +=1 

        cur_sign = [0] * (ord('z')-ord('a')+1)
        for i in range(m): cur_sign[ord(s2[i])-ord('a')] +=1 
        if cur_sign == target_sign : return True

        for i in range(m,n):
                cur_sign[ord(s2[i])-ord('a')] +=1
                cur_sign[ord(s2[i-m])-ord('a')] -=1
                if cur_sign == target_sign : return True

        return False
