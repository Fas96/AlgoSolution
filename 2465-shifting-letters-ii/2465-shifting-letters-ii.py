class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N = len(s)

        delta = [0] * (N + 1)
        for left, right, direction in shifts:
            if direction == 0:
                direction = -1

            delta[left] += direction
            delta[right + 1] -= direction

        ans = []
        current_delta = 0

        for i in range(N):
            current = ord(s[i]) - ord('a')
            current_delta += delta[i]
            current += current_delta
            current %= 26

            ans.append(chr(current + ord('a')))
        return "".join(ans)