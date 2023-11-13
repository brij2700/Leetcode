class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=set('aeiouAEIOU')
        vowelMap=defaultdict(int)
        for i in s:
            if i in vowels:
                vowelMap[i]+=1
        sortedVowelList="AEIOUaeiou"
        vowelList=[]
        for i in sortedVowelList:
            for j in range(vowelMap[i]):
                vowelList.append(i)
        idx=0
        i=0
        stringList=[i for i in s]
        while(idx<len(vowelList)):
            if s[i] in vowels:
                stringList[i]=vowelList[idx]
                idx+=1
            i+=1
        return ''.join(stringList)
        
        