class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans=[folder[0]]
        n=len(folder)
        for i in range(1,n):
            if not folder[i].startswith(ans[-1]+"/"):
                ans.append(folder[i])
        return ans