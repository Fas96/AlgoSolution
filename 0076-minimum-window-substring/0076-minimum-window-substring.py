class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Create a dictionary to store the frequency of characters in t
        t_count = Counter(t)

        # Initialize pointers and variables to track the window
        left, right = 0, 0
        required_chars = len(t)
        min_len = float('inf')
        min_window_start = 0

        while right < len(s):
            # If the current character is in t, decrement the required count
            if t_count[s[right]] > 0:
                required_chars -= 1

            # Decrease the frequency of the current character in t_count
            t_count[s[right]] -= 1
            right += 1

            # Check if all characters from t are included in the window
            while required_chars == 0:
                # Update the minimum window if the current window is smaller
                if right - left < min_len:
                    min_len = right - left
                    min_window_start = left

                # Increase the frequency of the character at the left pointer
                t_count[s[left]] += 1

                # If the character at the left pointer is in t, increment the required count
                if t_count[s[left]] > 0:
                    required_chars += 1

                # Move the left pointer to the right
                left += 1

        # If no valid window is found, return an empty string
        return "" if min_len == float('inf') else s[min_window_start:min_window_start + min_len]
        