class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time=[dist[i]/speed[i] for i in range(len(speed))]
        time.sort()
        ans=0
        for i in range(len(time)):
            if time[i]<=i:
                break
            ans+=1
        return ans
        