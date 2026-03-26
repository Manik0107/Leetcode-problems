class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        longest = 0
        nums_zeros = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                nums_zeros += 1

            while nums_zeros > k:
                if nums[l] == 0:
                    nums_zeros -= 1
                l += 1
 
            longest = max(longest, (i - l) + 1 )
        return longest