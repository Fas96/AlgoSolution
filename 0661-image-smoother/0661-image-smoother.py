class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])

        def getValue(i: int, j: int)-> int:
            return 0 if (i < 0 or j < 0) else img[i][j]
        
        for i, row in enumerate(img):
            for j, value in enumerate(row):
                img[i][j] += getValue(i-1,j) + getValue(i,j-1) - getValue(i-1,j-1)
        
        newImage = [[0 for val in row] for row in img]

        def calculateSmoothValue(i: int, j: int)-> int:
            total = getValue(min(i+1, m-1), min(j+1, n-1))
            left = getValue(min(i+1, m-1), j-2)
            top = getValue(i-2, min(j+1, n-1))
            topLeft = getValue(i-2, j-2)

            totalElem = (min(i+2, m) - max(i-1, 0)) * (min(j+2, n) - max(j-1, 0))

            return (total - left - top + topLeft) // totalElem

        for i, row in enumerate(newImage):
            for j, value in enumerate(row):
                newImage[i][j] = calculateSmoothValue(i, j)
        
        return newImage