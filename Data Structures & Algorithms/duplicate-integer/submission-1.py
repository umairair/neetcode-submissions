class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hash set cannot include duplicate elements
        # iterate through array and add things to hashset if they're not already
        # each time we add something we do a check using a hash set function      to     see if the element is already in there
        # if it is, return true, if not keep going
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            else:
                hash_set.add(num)
        return False
        