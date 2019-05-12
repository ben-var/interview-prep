class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        special_groups = set()
        
        # by sorting the even and odd characters, special equivalent
        # words are uniformly represented. S
        for word in A:
            evens = "".join(sorted(word[::2]))
            odds = "".join(sorted(word[1::2]))
            special_groups.add(evens + odds)
        
        return len(special_groups)
            