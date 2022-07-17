class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        K=k
        N=n
        MOD = 10**9 + 7
        ds = [0] + [1] * (K + 1)
        for n in xrange(2, N+1):
            new = [0]
            for k in xrange(K+1):
                v = ds[k+1]
                v -= ds[k-n+1] if k >= n else 0
                new.append( (new[-1] + v) % MOD )
            ds = new
        return (ds[K+1] - ds[K]) % MOD