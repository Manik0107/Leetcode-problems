class Solution:
    def trap(self, height: List[int]) -> int:
        arr = [0] * len(height)
        ans = 0
        arr[0] = height[0]
        for i in range(1, len(height)):
            arr[i] = max(arr[i-1], height[i])

        right_max = height[len(height)-1]
        for i in range(len(height)-1, -1, -1):
            right_max = max(right_max, height[i])
            arr[i] = min(arr[i], right_max)

        for i in range(len(height)):
            ans += arr[i] - height[i]
        
        return ans