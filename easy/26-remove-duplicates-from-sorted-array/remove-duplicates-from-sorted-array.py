class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if not (nums[i - 1] ^ nums[i]):
                nums.remove(nums[i - 1])
                continue
            i += 1
        return i