class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_sum = 0
        l_sum = 0
        r_sum = 0
        r = len(cardPoints) -1 
        for i in range(k):
            l_sum += cardPoints[i]
        max_sum = l_sum

        for i in range(k-1, -1, -1):
            l_sum -= cardPoints[i]
            r_sum += cardPoints[r]
            r -= 1
            max_sum = max(max_sum, l_sum + r_sum)

        return max_sum
        