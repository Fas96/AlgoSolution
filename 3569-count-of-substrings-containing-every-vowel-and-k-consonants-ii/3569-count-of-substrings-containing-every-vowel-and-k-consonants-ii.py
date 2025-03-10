class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def contain_more_then(k):
            vowels = set('aeiou')
            vowels_map = defaultdict(int)
            consonants = 0
            res = 0
            l = 0
            for r in range(len(word)):
                if word[r] in vowels:
                    vowels_map[word[r]] += 1
                else:
                    consonants += 1

                while len(vowels_map) == 5 and k <= consonants:
                    res += (len(word) - r)
                    if word[l] in vowels:
                        vowels_map[word[l]] -= 1
                        if vowels_map[word[l]] == 0:
                            vowels_map.pop(word[l])
                    else:
                        consonants -= 1

                    l += 1

            return res

        return contain_more_then(k) - contain_more_then(k + 1)
                