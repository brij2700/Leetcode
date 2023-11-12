class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stops=defaultdict(set)
        buses=defaultdict(set)
        for i,route in enumerate(routes):
            for stop in route:
                stops[stop].add(i)
                buses[i].add(stop)
        minbuses=float('inf')
        visited={}
        travelled={}
        def travel(source,destination,cur):
            nonlocal minbuses
            if minbuses<=cur:
                return
            if source in visited:
                if visited[source]<=cur:
                    return
            visited[source]=cur
            for bus in stops[source]:
                if bus in travelled:
                    if travelled[bus]<=cur:
                        continue
                travelled[bus]=cur
                cur+=1
                if destination in buses[bus]:
                    minbuses=min(cur,minbuses)
                    return
                for stop in buses[bus]:
                    travel(stop,destination,cur)
                cur-=1
        if source==target:
                return 0
        travel(source,target,0)
        return minbuses if minbuses!=float('inf') else -1


        