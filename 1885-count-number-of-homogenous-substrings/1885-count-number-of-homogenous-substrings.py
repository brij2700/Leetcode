class Solution:
    def countHomogenous(self, s: str) -> int:
        l,r=0,0
        ans=0
        cur_char=s[l]
        while(r<len(s)):

                if s[r]!=cur_char:
                    ans+=(r-l)*(r-l+1)/2
                    l=r
                    cur_char=s[l]
                    r+=1
                else:
                    r+=1
        ans+=(r-l)*(r-l+1)/2
        return int(ans)%(10**9+7)

        