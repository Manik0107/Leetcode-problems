class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        def get_sum(is_min):
            stack = []
            left = [0] * n
            right = [0] * n

            for i in range(n):
                while stack and (
                    nums[stack[-1]] > nums[i] if is_min else nums[stack[-1]] < nums[i]
                ):
                    stack.pop()
                left[i] = i - (stack[-1] if stack else -1)
                stack.append(i)

            stack = []
            for i in range(n - 1, -1, -1):
                while stack and (
                    nums[stack[-1]] >= nums[i] if is_min else nums[stack[-1]] <= nums[i]
                ):
                    stack.pop()
                right[i] = (stack[-1] if stack else n) - i
                stack.append(i)

            total = 0
            for i in range(n):
                total += nums[i] * left[i] * right[i]

            return total

        return get_sum(False) - get_sum(True)