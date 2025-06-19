class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj=defaultdict(list)
        for a,b in connections:
            adj[a].append(b)
            adj[b].append(a)
        visited=set()
        discoveryTime=[-1]*n
        lowLinkTime=[-1]*n
        
        criticalEdges=[]
        def dfs(node,parent,time):
            visited.add(node)
            discoveryTime[node]=time
            lowLinkTime[node]=time
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor,node,time+1)
                    lowLinkTime[node]=min(lowLinkTime[node],lowLinkTime[neighbor])

                    if lowLinkTime[neighbor]>discoveryTime[node]:
                        criticalEdges.append([node,neighbor])
                elif neighbor!=parent:
                    lowLinkTime[node]=min(lowLinkTime[node],discoveryTime[neighbor])
        dfs(0,-1,0)
        return criticalEdges
