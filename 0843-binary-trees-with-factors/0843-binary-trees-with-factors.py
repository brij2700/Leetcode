class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        memo={}
        products = defaultdict(list)
        productsset=set(arr)
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i]*arr[j] in productsset:
                    products[arr[i]*arr[j]].append((arr[i],arr[j]))
        init={x:1 for x in arr}
        memo={}
        def createtree(num):
            if num in memo:
                return memo[num]
            if num in products:
                for prod in products[num]:
                   
                   init[num]+=createtree(prod[0])*createtree(prod[1])
            memo[num]=init[num]    
            return memo[num]
            
        
        ans=0
        arr.sort()
        print(products)
        for i in arr:
            
            x=createtree(i)
            print(x,i)
            ans+=x
        return ans%(10**9+7)