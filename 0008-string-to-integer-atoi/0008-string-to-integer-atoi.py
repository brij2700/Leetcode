class Solution:
    def myAtoi(self, s: str) -> int:
        ans=0
        sign=1
        checker=set("0123456789")
        MAX_INT=2**31 -1
        MIN_INT=-2**31
        i=0
        if len(s)<1:
            return 0 
        while i < len(s) and s[i] == " ":
                i+=1
                continue

        if i<len(s) and s[i] == '-' :
            i+=1
            sign=-1
           
        elif i<len(s) and s[i] == '+':
            i+=1
           
        while i < len(s):
            if s[i] in checker:
                ans=ans*10 + int(s[i])
                i+=1
            else:
                break
        ans=sign*ans
        if ans < 0:
            return max(ans,MIN_INT)
        else:
            return min(ans,MAX_INT)
            
            
        
                
            
        