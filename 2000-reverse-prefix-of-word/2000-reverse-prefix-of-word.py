class Solution(object):
    def reversePrefix(self, word, ch):
        idx=word.find(ch)
        print(idx)
        if idx:
            return word[:idx+1][::-1]+word[idx+1:]
        return word
        