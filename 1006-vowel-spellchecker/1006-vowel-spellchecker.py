class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def remove_vowels(s):
            chars = list(s)
            for i in range(len(chars)):
                if chars[i] in 'aeiou':
                    chars[i] = '*'
            return ''.join(chars)
        
        word_set = set(wordlist)
        
        lowercase_map = {}
        for word in wordlist:
            lowercase_word = word.lower()
            if lowercase_word not in lowercase_map:
                lowercase_map[lowercase_word] = word
        
        vowels_map = {}
        for word in wordlist:
            vowel_word = remove_vowels(word.lower())
            if vowel_word not in vowels_map:
                vowels_map[vowel_word] = word
        
        result = []
        for query in queries:
            if query in word_set:
                result.append(query)
            else:
                lowercase_word = query.lower()
                if lowercase_word in lowercase_map:
                    result.append(lowercase_map[lowercase_word])
                else:
                    vowel_word = remove_vowels(lowercase_word)
                    if vowel_word in vowels_map:
                        result.append(vowels_map[vowel_word])
                    else:
                        result.append("")
        
        return result