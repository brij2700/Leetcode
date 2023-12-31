class Solution:
    def romanToInt(self, s: str) -> int:
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sumtotal=0
        for i in range (0,len(s)):
            if i != len(s)-1:
                if roman[s[i]]<roman[s[i+1]]:
                    sumtotal-=roman[s[i]]
                    continue
            sumtotal+=roman[s[i]]
        return sumtotal
            