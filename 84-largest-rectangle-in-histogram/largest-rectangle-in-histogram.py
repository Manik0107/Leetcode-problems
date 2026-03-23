class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                ele = heights[stack[-1]]
                stack.pop()
                nse = i
                pse = stack[-1] if stack else -1
                maxarea = max(maxarea, ele * (nse - pse - 1))

            stack.append(i)
        while stack:
            ele = heights[stack[-1]]
            stack.pop()
            nse = len(heights)
            pse = stack[-1] if stack else -1
            maxarea = max(maxarea, ele * (nse - pse - 1))

        return maxarea
        
