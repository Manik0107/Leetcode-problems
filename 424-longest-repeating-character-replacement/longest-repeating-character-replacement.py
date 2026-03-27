class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = longest = 0
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - 65] += 1

            while (i - l + 1) - max(count) > k:
                print(max(count))
                count[ord(s[l]) - 65] -= 1
                l += 1

            longest = max(longest, (i - l + 1))

        return longest
