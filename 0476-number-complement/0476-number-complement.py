class Solution:
    def findComplement(self, num: int) -> int:
        an=""
        for c in str(bin(num)[2:]):
            print(c)
            if c=='1':
                an+='0'
            else:
                an+='1'
        print(an)

        return int( eval('0b' + an))
        