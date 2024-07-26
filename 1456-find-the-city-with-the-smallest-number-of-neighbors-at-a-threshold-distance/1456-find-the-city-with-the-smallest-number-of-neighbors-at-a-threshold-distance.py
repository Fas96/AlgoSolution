class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        mp={i:[] for i in range(n)}
        for f,t ,v in edges:
            mp[f].append((t,v))
            mp[t].append((f,v))
        
        def dijksta(start): 
            distances = [float('inf')] * n
            distances[start] = 0
            priority_queue = [(0, start)]
            
            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)
                if current_distance > distances[current_node]:
                    continue
                for neighbor, weight in mp[current_node]:
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))
            return distances

        count = [0] * n
        res = 0
        for c in range(n):
            distance = dijksta(c) 
            count[c] = sum(1 if dis <= distanceThreshold else 0 for dis in distance)
            res = c if count[c] <= count[res]  else  res
   
        return res


        return 0
        