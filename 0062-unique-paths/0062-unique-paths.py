class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m_fact = factorial(m-1)
        n_fact = factorial(n-1)
        return factorial(n+m-2)//(m_fact*n_fact)