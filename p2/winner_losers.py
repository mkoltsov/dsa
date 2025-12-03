from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners=defaultdict(int)
        losers=defaultdict(int)
        win=[]
        lose=[]
        for i in matches:
            print(i)
            winners[i[0]] += 1
            losers[i[1]] += 1

        for i in winners.keys():
            if i not in losers:
                print(f"winner{i}")
                win.append(i)
        for i in losers.items():
            if i[1]==1:
                lose.append(i[0])         
            # print(f"winners {i}")
            # if i[1]==len(matches):
            #     print(i)
            #     print("Yay")

        print(winners)
        print(losers)
        print(win)
        print(lose)
        return [win, lose]
Solution().findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])


