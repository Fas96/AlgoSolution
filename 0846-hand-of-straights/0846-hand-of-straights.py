class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:return False
        freq=Counter(hand)
        for i in sorted(freq):
            if freq[i] > 0:
                for j in range(groupSize)[::-1]:
                    freq[i + j] -= freq[i]
                    if freq[i + j] < 0:
                        return False
        return True
        