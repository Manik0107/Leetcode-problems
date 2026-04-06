class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(n-1):
            res = ""
            count = 1
            for i in range(len(result)):
                if i + 1 < len(result) and result[i] == result[i+1]:
                    count += 1
                else:
                    res += str(count) + result[i]
                    count = 1

            result = res
        return result 