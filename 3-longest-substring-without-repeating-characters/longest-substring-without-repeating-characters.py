class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        l = 0
        longest = 0

        for r in range(len(s)):
            if s[r] in last_seen:
                l = max(l, last_seen[s[r]] + 1)

            last_seen[s[r]] = r
            longest = max(longest, r - l + 1)

        return longest
