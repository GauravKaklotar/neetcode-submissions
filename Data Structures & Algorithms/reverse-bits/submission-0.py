class Solution:
    def reverseBits(self, n: int) -> int:

        ans = 0

        for _ in range(32):
            # Take the rightmost bit of n
            bit = n & 1

            # Shift ans left and add that bit
            ans = (ans << 1) | bit

            # Move to the next bit of n
            n >>= 1

        return ans