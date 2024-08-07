class Solution(object): 
    nums = [ "", "One", "Two", "Three", "Four",  "Five", "Six", "Seven", "Eight", "Nine" ]
    ten2_19 = [ "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",  "Fifteen", "Sixteen", "Seventeen", "Eighteen",  "Nineteen" ]
    morethan20 = [ "", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety" ]
    names = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        res = ""
        for i in range(4):
            if num == 0:
                break
            v = (self.get(num % 1000) + " " + self.names[i]).strip()
            if v == self.names[i]:
                v = ""
            res = (v + " " + res).strip()
            num //= 1000
        return res

    def get(self, num):
        tensandones = num % 100
        hundreds = num // 100
        res = ""
        if hundreds > 0:
            res = self.nums[hundreds] + " Hundred"
        num %= 100

        if tensandones > 0:
            if 10 <= tensandones <= 19:
                res += " " + self.ten2_19[tensandones - 10]
            else:
                res += " " + (self.morethan20[tensandones // 10] + " " + self.nums[tensandones % 10]).strip()

        return res.strip()