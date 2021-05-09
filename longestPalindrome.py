#https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
      n=len(s)
      dp=[[False]*(n-i) for i in range(n)]
      start, end=0,0
      for i in range(n):
        dp[i][0]=True
        if i!=n-1: 
          dp[i][1]=(s[i]==s[i+1])
          if dp[i][1]: start,end=i,i+1
      
      m=2
      
      
      while m<n:
        for i in range(0,n-m):
          dp[i][m]= (s[i]==s[i+m]) and dp[i+1][m-2]
          if dp[i][m]: start,end=i,i+m
        m+=1
      
      return s[start:end+1]
      

