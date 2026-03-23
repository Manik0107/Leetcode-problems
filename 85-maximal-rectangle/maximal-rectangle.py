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

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        area = [0] * len(matrix[0])
        maxarea = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    area[j] += 1
                else:
                    area[j] = 0
            maxarea = max(maxarea, self.largestRectangleArea(area))
        return maxarea