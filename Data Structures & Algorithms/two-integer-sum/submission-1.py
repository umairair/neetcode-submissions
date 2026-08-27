class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # every input has exactly one pair of numbers that add up to the target,
        # we need to find it.
        # specifically the indexes of these 2 numbers in the list with the smaller
        # one first like output example: [0,1]
        differences = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in differences:
                return [differences[difference], i]
            else:
                differences[nums[i]] = i
                
        