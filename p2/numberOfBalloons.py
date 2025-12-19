# from collections import defaultdict
# class Solution:
    # def maxNumberOfBalloons(self, text: str) -> int:
    #     ch=defaultdict(int)
    #     ballon=defaultdict(int)
    #     word="balloon"
    #     for c in text:
    #         ch[c] +=1

    #     for i in word:
    #          ballon[i] +=1

    #     matches_letters=0
    #     matches_words=0
    #     # print(ch)
    #     # print(ballon)
    #     exhausted=False
    #     while (exhausted==False):
    #         for k,v in ballon.items():
    #             if k not in ch:
    #                 return 0
    #             else:
    #                 if ch[k]==v:
    #                     ch[k]-=v
    #                     if ch[k]<v:
    #                         exhausted=True
    #                 matches_letters+=1   
    #         print(ch)
    #         print(matches_letters)
    #         if matches_letters==len(ballon):
    #             matches_words+=1
           
    #     return matches_words         

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        count = Counter(text)                    # Count letters in text
        balloon = Counter("balloon")             # {'b':1, 'a':1, 'l':2, 'o':2, 'n':1}

        # For each letter in "balloon", how many full sets can we make?
        return min(
            count['b'] // 1,
            count['a'] // 1, 
            count['l'] // 2,
            count['o'] // 2,
            count['n'] // 1
        )       

print(Solution().maxNumberOfBalloons("loonbalxballpoon"))