class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_parentheses = 0
        close_needed = 0
        for char in s:
            if char == "(":
                open_parentheses += 1
            else:
                if open_parentheses > 0:
                    open_parentheses -= 1
                else:
                    close_needed += 1
        return open_parentheses + close_needed