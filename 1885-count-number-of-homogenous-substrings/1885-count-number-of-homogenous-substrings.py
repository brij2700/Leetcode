class Solution:
    def countHomogenous(self, s: str) -> int:
        l,r=0,0
        ans=0
        while(r<len(s)):
            if l==r:
                cur_char=s[l]
                r+=1
            else:
                if s[r]!=cur_char:
                    ans+=(r-l)*(r-l+1)/2
                    l=r
                else:
                    r+=1
        ans+=(r-l)*(r-l+1)/2
        return int(ans)%(10**9+7)

        