class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        maxHeap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(maxHeap)
        ans = []
        
        while len(maxHeap) >= 2:
            count1, char1 = heapq.heappop(maxHeap)
            count2, char2 = heapq.heappop(maxHeap)
            
            ans.extend([char1, char2])
            
            if count1 + 1 < 0:
                heapq.heappush(maxHeap, (count1 + 1, char1))
            if count2 + 1 < 0:
                heapq.heappush(maxHeap, (count2 + 1, char2))
        
        if maxHeap:
            count, char = heapq.heappop(maxHeap)
            if -count > 1:
                return ""
            ans.append(char)
        
        return ''.join(ans)

        