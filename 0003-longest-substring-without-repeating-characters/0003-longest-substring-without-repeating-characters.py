class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char={}
        start=0
        maxlen=0
        for i,j in enumerate(s):
            if j in char and char[j]>=start:
                maxlen=max(maxlen,i-start)
                start=char[j]+1
            char[j]=i
        maxlen=max(maxlen,len(s)-start)
        return maxlen

        
