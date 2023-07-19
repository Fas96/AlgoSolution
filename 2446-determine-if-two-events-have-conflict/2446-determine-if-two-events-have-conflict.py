class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        ans = False 
        event1Start = int(event1[0][:2]) * 60 + int(event1[0][3:])
        event1End = int(event1[1][:2]) * 60 + int(event1[1][3:])
        event2Start = int(event2[0][:2]) * 60 + int(event2[0][3:])
        event2End = int(event2[1][:2]) * 60 + int(event2[1][3:])
        
        if event1Start <= event2Start:
            if event1End >= event2Start:
                ans = True
        elif event1Start >= event2Start:
            if event2End >= event1Start:
                ans = True
        else:
            ans = True
            
        return ans