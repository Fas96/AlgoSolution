class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
         
        L,R=0,len(image)-1
        while L<=R:
            row=image[L] 
            image[L]=row[::-1]
            tm=[]
            for r in image[L]:
                tm.append(r^1)
            image[L]=tm
            L+=1
          
        return image 