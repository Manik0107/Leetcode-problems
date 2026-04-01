class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            count = {}
            left = 0
            res = 0
            
            for right in range(len(nums)):
                if nums[right] not in count:
                    count[nums[right]] = 0
                    k -= 1
                count[nums[right]] += 1
                
                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                        k += 1
                    left += 1
                
                res += right - left + 1
            
            return res
        
        return atMost(k) - atMost(k - 1)