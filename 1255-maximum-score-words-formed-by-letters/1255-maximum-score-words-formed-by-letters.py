class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def bt(i) -> None:
            nonlocal ans
            if i == len(words): # reach terminal
                total = 0
                c2f = Counter()
                for ind in inds:
                    for c in words[ind]:
                        c2f[c] += 1
                        total += score[ord(c) - ord('a')]
                        if c2f[c] > letter_count[c]: # impossible
                            return
                ans = max(ans, total)
                return
            
            # take
            inds.append(i)
            bt(i + 1)
            inds.pop()

            # skip
            bt(i + 1)
        

        letter_count = Counter(letters)
        ans = 0
        inds = []
        bt(0)
        return ans