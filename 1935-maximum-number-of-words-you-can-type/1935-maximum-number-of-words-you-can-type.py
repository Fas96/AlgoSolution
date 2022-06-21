class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        an = []
        for w in text.split(" "):
            c = 0
            for b in brokenLetters:
                if b not in w:
                    c += 1
            if c == len(brokenLetters):
                an.append(w)
        return len(an)