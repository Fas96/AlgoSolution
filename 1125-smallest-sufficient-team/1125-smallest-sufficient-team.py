class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        res = [''] * 17
        n = len(req_skills)
        def dfs(idx, has, path):
            nonlocal res
            if idx == n:
                res = path
            elif req_skills[idx] in has:
                dfs(idx + 1, has, path)
            else:
                if len(path) + 1 < len(res):
                    for i, p in enumerate(people):
                        p = set(p)
                        if req_skills[idx] in p:
                            union = p & has
                            has |= p
                            dfs(idx + 1, has, path + [i])
                            has -= p
                            has |= union
        dfs(0, set(), [])
        return res