class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result = 0
        dictionary = {"a" : -1,
        "b":-1,
        "c":-1}
        for n, i in enumerate(s):
            dictionary[i] = n
            if min(dictionary.values()) > -1:
                result += min(dictionary.values()) + 1
        return result