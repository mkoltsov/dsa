from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ch=defaultdict(str)
        ballon=defaultdict(str)
        word="balloon"
        for c in text:
            ch[c] +=1

        for i in word:
             ballon[i] +=1

        matches=0
        for k,v in ballon.items():
            if k not in ch:
                return 0
            else:
                if ch[k]==v:
                    matches+=1
        if matches==len(word):
            return 1
        else:
            return 0            

print(Solution().maxNumberOfBalloons("nlaebolko"))