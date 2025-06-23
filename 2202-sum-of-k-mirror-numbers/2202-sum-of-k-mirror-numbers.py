class Solution:
    def kMirror(self, k: int, n: int) -> int:
        left = 1
        count = 0
        answer = 0
        while count < n:
            right = left * 10
            for op in range(2):
                i = left
                while i < right and count < n:
                    combined = i
                    x = (i // 10) if op == 0 else i
                    while x > 0:
                        combined = combined * 10 + (x % 10)
                        x = x // 10
                    if self.is_palindrome(combined, k):
                        count += 1
                        answer += combined
                    i += 1
            left = right
        return answer

    def is_palindrome(self, x: int, k: int) -> bool:
        s = self.to_base_k(x, k)
        return s == s[::-1]

    def to_base_k(self, num: int, k: int) -> str:
        if num == 0:
            return "0"
        digits = []
        while num > 0:
            digits.append(str(num % k))
            num = num // k
        return ''.join(reversed(digits))