class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverseNum=0
        originalNum=x
        if x<0:
            return False
        while(x>0):
            reverseNum=reverseNum*10 + x%10
            x=x//10
        return(reverseNum==originalNum)    
        