class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res1 = [0] * len(nums2)
        stack = []
        res2 = [0] * len(nums1)
        for i in range(len(nums2) -1, -1, -1):
            if not stack:
                stack.append(nums2[i])
                res1[i] = -1
            elif stack[-1] > nums2[i]:
                res1[i] = stack[-1]
                stack.append(nums2[i])
            else:
                while stack and stack[-1] <= nums2[i]:
                    stack.pop()
                if stack:
                    res1[i] = stack[-1]
                    stack.append(nums2[i])
                else:
                    res1[i] = -1
                    stack.append(nums2[i])

        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            res2[i] = res1[index]
            
        return res2