from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        arr = [0] * n
        ans = 0

        arr[0] = height[0]
        for i in range(1, n):
            arr[i] = max(arr[i-1], height[i])

        right_max = height[n-1]
        for i in range(n-1, -1, -1):
            right_max = max(right_max, height[i])
            arr[i] = min(arr[i], right_max)

        for i in range(n):
            ans += arr[i] - height[i]

        return ans