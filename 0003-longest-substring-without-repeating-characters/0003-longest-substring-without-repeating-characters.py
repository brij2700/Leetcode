class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        h={}
        start=0
        maxlen=0
        for i in range(len(s)):
            
            if s[i] in h and h[s[i]]>=start:
                #start=1
                start=h[s[i]]+1
            maxlen=max(maxlen,i-start+1)
            #maxlen=3
            h[s[i]]=i
        return maxlen

                
                                                        
            
            
            
        