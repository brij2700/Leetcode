class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        hash_map=defaultdict(list)
        for pair in adjacentPairs:
            hash_map[pair[0]].append(pair[1])
            hash_map[pair[1]].append(pair[0])
        visited=set()
        ans=[]
        def createarray(num):
            if num in visited:
                return
            ans.append(num)
            visited.add(num)
            for i in hash_map[num]:
                createarray(i)
            return
        for i in hash_map:
            if len(hash_map[i])==1:
                createarray(i)
                break
        return ans