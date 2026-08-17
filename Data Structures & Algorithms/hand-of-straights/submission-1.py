class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        n = len(hand)

        if n % groupSize != 0:
            return False
        
        from collections import Counter

        counter = Counter(hand)

        for key in sorted(counter):

            freq = counter[key]

            for val in range(key, key + groupSize):
                if counter[val] < freq:
                    return False
                
                counter[val] -= freq
        
        return True

'''
Why subtract freq?

Suppose:

count:
1 → 2
2 → 2
3 → 2
4 → 2

The smallest card is 1, and there are 2 copies of it.

Therefore we need to create 2 groups:

1 2 3 4
1 2 3 4

So we subtract 2 from each:

1 → 0
2 → 0
3 → 0
4 → 0

This is much more efficient than creating one group at a time.
'''