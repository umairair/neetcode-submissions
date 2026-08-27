class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if we know the length of 2 strings is the same, we only care about the
        # frequency of each character
        # possible solution:
        # 1. group together equal length strings 
        # 2. further group each of those by equal char frequency

        groups = {}
        for i in range(len(strs)):
            char_freq = [0] * 26
            for char in strs[i]:
                char_freq[ord(char) - ord('a')] += 1
            key = tuple(char_freq)
            if key in groups:
                groups[key].append(strs[i])
            else:
                groups[key] = [strs[i]]
            

        return list(groups.values())
           
            






