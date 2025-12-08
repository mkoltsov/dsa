from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ch=defaultdict(str)
        word="balloon"
        for c in text:
            ch[c] +=1

        while     