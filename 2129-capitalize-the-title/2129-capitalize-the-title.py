class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        tstr = title.split(" ")
        rs = ""
        for w in tstr:
            if len(w) > 2:
                rs = rs + " " + w.capitalize()
            else:
                rs =rs+" " +w.lower()
        
        return rs.strip()