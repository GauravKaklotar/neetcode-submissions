class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        x, y, z = target

        found_x, found_y, found_z = False, False, False

        for a, b, c in triplets:

            # This triplet can never be part of target
            if a > x or b > y or c > z:
                continue
            
            if found_x and found_y and found_z:
                return True
            
            if a == x:
                found_x = True
            
            if b == y:
                found_y = True
            
            if c == z:
                found_z = True
        
        return found_x and found_y and found_z