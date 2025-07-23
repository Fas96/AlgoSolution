class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        points = 0
        
        def remove_and_count(s, sub, point):
            count = 0
            while sub in s:
                num_sub = s.count(sub)
                count += num_sub
                s = s.replace(sub, '', num_sub)
            return s, count * point
        
        if y > x:
            s, gained = remove_and_count(s, 'ba', y)
            points += gained
            s, gained = remove_and_count(s, 'ab', x)
            points += gained
        else:
            s, gained = remove_and_count(s, 'ab', x)
            points += gained
            s, gained = remove_and_count(s, 'ba', y)
            points += gained
        
        return points