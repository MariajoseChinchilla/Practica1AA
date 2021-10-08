#find de subaray with max sum

class Solution:
    def maxSubArray(self,nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] = nums[i] + nums[i-1]       #sumamos solo los que aportan, positivos

        maxsum = max(nums)
        return maxsum

