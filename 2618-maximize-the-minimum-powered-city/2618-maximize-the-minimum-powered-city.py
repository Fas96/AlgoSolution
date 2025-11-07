class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        def ok(x):
            add = [0]*(n+1)
            s, kx = 0, k
            for i in range(n):
                s += add[i]
                if power[i]+s < x:
                    need = x - (power[i]+s)
                    if need > kx:
                        return False
                    kx -= need
                    s += need
                    if i+2*r+1 < n:
                        add[i+2*r+1] -= need
            return True
        n = len(stations)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stations[i]
        power = [0]*n
        for i in range(n):
            power[i] = prefix[min(n-1, i+r)+1] - prefix[max(0, i-r)]

        low, high = 0, sum(stations)+k
        while low < high:
            mid = (low+high+1)//2
            if ok(mid):
                low = mid
            else:
                high = mid-1
        return low