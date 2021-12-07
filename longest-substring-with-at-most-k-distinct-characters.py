# 340. Longest Substring with At Most K Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

class Solution:   
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0: return 0
        
        s = [w for w in s]
        ord_max = max([ord(w) for w in s])
        ord_min = min([ord(w) for w in s])
        freq_table = [0] * (ord_max-ord_min+1)
        
        cur_string = []
        cur_lenght, max_length, cur_distinct  = 0, 0, 0

        while s:
            w = s.pop()
            cur_string.append(w)
            cur_lenght += 1
            freq_table[ord(w)-ord_min] +=1
            if freq_table[ord(w)-ord_min] == 1: cur_distinct += 1   #new char

            if cur_distinct <= k: #update max_length
                max_length = max(max_length, cur_lenght)

            else: #delete left chars
                while cur_distinct > k and cur_lenght:
                    w = cur_string.pop(0)
                    cur_lenght -= 1
                    freq_table[ord(w)-ord_min] -=1
                    if freq_table[ord(w)-ord_min] == 0: cur_distinct -= 1

        return max_length 
