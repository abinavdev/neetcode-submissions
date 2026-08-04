class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = set(nums)
        return len(n) != len(nums)
        # if len(n) == len(nums):
        #     return False
        # else:
        #     return True
                
        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)

        # return False