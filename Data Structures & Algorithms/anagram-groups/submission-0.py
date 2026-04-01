class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)

        from collections import defaultdict
        d = defaultdict(list)

        for str in strs:
            freq = [0] * 26

            for c in str:
                freq[ord(c) - ord('a')] += 1
            
            d[tuple(freq)].append(str)
        
        return list(d.values())