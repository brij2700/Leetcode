class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxvol=0
        while(l<r):
            #height[l]=1
            #height[r]=7
            if height[l]<height[r]:
                #maxvol=1
                maxvol=max(maxvol,(r-l)*height[l])
                #maxvol=8
                l+=1
            else:
                maxvol=max(maxvol,(r-l)*height[r])
                r-=1
        return maxvol

        