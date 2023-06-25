class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        @cache
        def dp(i, fuel):
            cnt = int(i == finish)
            for j in range(len(locations)):
                cost = abs(locations[i] - locations[j])
                if i != j and cost <= fuel:
                    cnt += dp(j, fuel - cost)
            return cnt % (10 ** 9 + 7)
        return dp(start, fuel)
        