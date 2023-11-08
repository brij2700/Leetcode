class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        max_diag=min(abs(sx-fx),abs(sy-fy))
        min_dist=abs(sx-fx)+abs(sy-fy)-max_diag
        if min_dist==0 and t==1:
            return False
        return min_dist<=t
    