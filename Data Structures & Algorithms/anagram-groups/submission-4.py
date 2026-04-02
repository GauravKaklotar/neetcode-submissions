class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # m = string_length
        # n = array_length

        # res = [(''.join(sorted(str)), str) for str in strs]
        # d = dict()

        # for sorted_s, s in res:
        #     if sorted_s in d:
        #         d[sorted_s].append(s)
        #     else:
        #         d[sorted_s] = [s]
        
        # return list(d.values())

        # Time: O(n * mlogm)
        # Space: O(N)
        


        n = len(strs)

        from collections import defaultdict
        d = defaultdict(list)

        for str in strs:
            freq = [0] * 26

            for c in str:
                freq[ord(c) - ord('a')] += 1
            
            d[tuple(freq)].append(str)
        
        return list(d.values())

        # Time: O(N*M)
        # Space: O(N)