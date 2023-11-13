class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=set('aeiouAEIOU')
        vowelList=[]
        for i in s:
            if i in vowels:
                vowelList.append(i)
        vowelList.sort()
        idx=0
        i=0
        stringList=[i for i in s]
        while(i<len(s) and idx<len(vowelList)):
            if s[i] in vowels:
                stringList[i]=vowelList[idx]
                idx+=1
            i+=1
        return ''.join(stringList)
        
        