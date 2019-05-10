class Solution:
    def findComplement(self, num: int) -> int:
        # XOR with bit mask of all '1' same bit-length as input
        # results in the complement
        mask = int("1" * len(bin(num)[2:]), 2)
        return num ^ mask