class WordFilter:

    def __init__(self, words: List[str]):
        prefixes = defaultdict(set)
        suffixes = defaultdict(set)
        indices = defaultdict(int)
        
		# Storing Indices
        for ind, word in enumerate(words):
            indices[word] = ind
            
            prefix = ""
            suffix = ""
            
			# Storing all prefixes
            for char in word:
                prefix += char
                prefixes[prefix].add(word)
            
			#Storing all suffixes
            for char in word[::-1]:
                suffix = char + suffix
                suffixes[suffix].add(word)
        
        self.prefixes = prefixes
        self.suffixes = suffixes
        self.indices = indices
                
                

    def f(self, prefix: str, suffix: str) -> int:
        prefixes = self.prefixes
        suffixes = self.suffixes
        indices = self.indices
        
		# intersection of prefixes[prefix] and suffixes[suffix]
        common_words = prefixes[prefix] & suffixes[suffix]
        
        max_index = -1
        for word in common_words:
            max_index = max(max_index, indices[word])
        
        return max_index