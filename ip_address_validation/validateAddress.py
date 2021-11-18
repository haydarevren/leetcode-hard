class Solution:
    def validateAddress(self, addresses: List[List[str]]) -> List[List[str]]:
      
      # explicit function to verify IPv4
      def isValidIPv4(s):

        # check number of periods
        if s.count('.') != 3:
          return 0
        l = list(map(str, s.split('.')))

        # check range of each number between periods
        octal=-1
        for ele in l:
          if int(ele) < 0 or int(ele) > 255:
            return 0
          if octal==1:
            for e in ele:
              if e == '9': return 0 
          if octal==0 and ele[0]=='0' and len(ele)!=1: return 0
          
          if ele[0]==0 and len(ele)!=1:
            for e in ele:
              if e == '9': return 0 
            
          if ele[0]==0 and len(ele)!=1:  octal=1
          for e in ele:
              if e == '9': octal=0

        return 1
      
      # explicit function to verify IPv6
      def isValidIPv6(s):
        l = list(map(str, s.split(':')))
        hexdigits = '0123456789abcdefABCDEF'
        for x in l:
            # Validate hexadecimal in range (0, 2**16):
            # 1. at least one and not more than 4 hexdigits in one chunk
            # 2. only hexdigits are allowed: 0-9, a-f, A-F
            if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                return 0
        return 1
      result=[]
      for IP in addresses:
        if IP.count('.') > 0 and  IP.count(':') == 0:
          if isValidIPv4(IP): result.append('IPv4')
          else: result.append('Neither')
            
        elif IP.count(':')>0 and  IP.count('.') == 0:
          if isValidIPv6(IP): result.append('IPv6')
          else: result.append('Neither')
            
        else: result.append('Neither')
          
       
      return result
