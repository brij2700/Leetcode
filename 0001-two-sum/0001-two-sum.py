class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_set={}
        for i,j in enumerate(nums):
            if target-j in hash_set:
                answer=[i,hash_set[target-j]]
                return answer
            hash_set[j]=i

                
