class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        userToLang = {u:{*langs} for u,langs in enumerate(languages, 1)}
        friendships = [f for f in friendships if not userToLang[f[0]]&userToLang[f[1]]]
 
        if not friendships: return 0

        return min(len({u for f in friendships for u in f if l not in userToLang[u]}) for l in range(1,n+1))