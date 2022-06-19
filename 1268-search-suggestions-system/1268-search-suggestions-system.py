class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        res=[]
        for i in range(len(searchWord)):
            ls=[]
            sub=searchWord[:i+1] 
            for word in products:
                if word.startswith(sub):
                    ls.append(word)
            res.append(sorted(list(set(ls)))[:3])
        return res
        