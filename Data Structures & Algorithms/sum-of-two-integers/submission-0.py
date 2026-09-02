class Solution:
    def getSum(self, a: int, b: int) -> int:

        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        return a if a <= MAX_INT else a - (MASK + 1)

'''
Core idea

For two binary numbers:

a ^ b → addition without carry
a & b → tells us where the carry occurs
(a & b) << 1 → moves the carry to the correct position

So:

sum_without_carry = a ^ b
carry             = (a & b) << 1

Then repeat until there is no carry.

Python solution

Python needs a little extra handling because Python integers don't have a fixed 32-bit representation.
'''