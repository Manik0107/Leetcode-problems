class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ple = [-1] * len(heights)
        n = len(heights)
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            ple[i] = stack[-1] if stack else -1
            stack.append(i)

        nle = [n] * n
        stack = []
        for i in range(n-1, -1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            nle[i] = stack[-1] if stack else n
            stack.append(i)

        maxi = heights[0]
        for i in range(n):
            length = nle[i] - ple[i] - 1
            maxi = max(maxi, heights[i] * length)
        
        return maxi