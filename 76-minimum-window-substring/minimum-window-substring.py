class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        required = len(t_count)

        l = 0
        formed = 0
        window_count = {}

        res = float("inf"), None, None

        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            while l <= r and formed == required:
                char = s[l]

                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)

                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1

                l += 1

        return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]