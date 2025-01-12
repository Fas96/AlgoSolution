class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        openings = []
        unlocked = []

        for i, char in enumerate(s):
            if locked[i] == "0":
                unlocked.append(i)
            elif char == "(":
                openings.append(i)
            else:  # char == ")"
                if openings:
                    openings.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        while openings and unlocked:
            if unlocked[-1] < openings[-1]:
                return False
            unlocked.pop()
            openings.pop()

        return not openings and len(unlocked) % 2 == 0