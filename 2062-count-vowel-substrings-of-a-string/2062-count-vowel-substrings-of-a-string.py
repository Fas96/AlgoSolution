class Solution(object):
    def countVowelSubstrings(self, word):
        ls = self.get_all_substrings(word) 
        cnt = 0
        klist = []
        for i in ls:
            if len(i) < 5:
                continue
            if self.allVowels(i):
                klist.append(i)

        for w in klist:
            if self.allFiveVowels(w):
                cnt += 1
        return cnt

    def allVowels(self, wd):
        vlid = ['a', 'e', 'i', 'o', 'u']
        for w in wd:
            if w not in vlid:
                return False
        return True

    def allFiveVowels(self, wd):
        vlid = ['a', 'e', 'i', 'o', 'u']
        cont = 0
        for v in vlid:
            if v in wd:
                cont += 1
        return cont == 5

    def get_all_substrings(self, input_string):
        length = len(input_string)
        return [input_string[i:j + 1] for i in range(length) for j in range(i, length)]