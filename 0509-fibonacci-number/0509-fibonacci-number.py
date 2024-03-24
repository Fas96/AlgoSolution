class Solution:
    def fib(self, n: int) -> int:
        MAX_SAVE = 3
        fib = [0] * MAX_SAVE

        def f(n):
            fib[0] = 0
            fib[1] = 1
            for i in range(2, n + 1):
                fib[i % MAX_SAVE] = fib[(i - 1) % MAX_SAVE] + fib[(i - 2) % MAX_SAVE]

            return fib[n % MAX_SAVE]
        return f(n)
 