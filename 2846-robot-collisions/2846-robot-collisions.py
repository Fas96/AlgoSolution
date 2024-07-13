class Solution:
    def survivedRobotsHealths(self, P: List[int], H: List[int], D: str) -> List[int]:
        
        ans = []
        for i in sorted(range(len(P)), key = lambda i: P[i]):
            if D[i] == 'R':
                ans.append(i)
            else:
                while ans and H[ans[-1]] < H[i]:
                    H[i] -= 1
                    H[ans.pop()] = 0
                if ans:
                    if H[ans[-1]] == H[i]:
                        H[ans.pop()] = 0
                    else:
                        H[ans[-1]] -= 1
                    H[i] = 0
        return [h for h in H if h]   
        