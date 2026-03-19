class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nge = [0] * len(nums)
        stack = []

        for i in range(2*len(nums)-1, -1, -1):
            while stack and stack[-1] <= nums[i%len(nums)]:
                stack.pop()
            if i < len(nums):
                nge[i] = stack[-1] if stack else -1
            stack.append(nums[i%len(nums)])

        return nge
