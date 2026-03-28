class Solution:
    def f(self, nums: List[int], goal: int) -> int:
        count =0
        sum=0
        l=0
        if goal < 0:
            return 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum > goal:
                sum -= nums[l]
                l += 1
            count += (r - l + 1)
        return count
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.f(nums, goal) - self.f(nums, goal-1)
