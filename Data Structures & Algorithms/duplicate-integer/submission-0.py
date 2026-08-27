class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # sort 
        # then iterate over the array and check if neighbours are equal
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        