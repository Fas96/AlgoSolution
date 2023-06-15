class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort(key=lambda x: (-x[0], x[1]))
        wChar, maxDef = 0, 0 
        for _, defense in properties:
            if maxDef > defense:
                wChar += 1
            else:
                maxDef = defense
        return wChar
        