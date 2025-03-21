class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        dic = {recipes[i] : ingredients[i] for i in range(len(ingredients))}
        to_add, res = [], []

        start = True
        while to_add or start:
            start = False

            
            for i in to_add:
                del dic[i]
                supplies.add(i)
                res.append(i)
 
            to_add = []
            for key, val in dic.items():
                can_make = True
                for i in val:
                    if i not in supplies:
                        can_make = False
                        break
                if can_make:
                    to_add.append(key)
        return res