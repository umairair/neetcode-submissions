class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        groups = defaultdict(list)
        for i in range(len(strs)):
            char_freq = [0] * 26
            for char in strs[i]:
                char_freq[ord(char) - ord('a')] += 1
          
           
            groups[tuple(char_freq)].append(strs[i])
            
            

        return list(groups.values())