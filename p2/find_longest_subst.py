from collections import defaultdict
from time import sleep

def find_longest_substring(s, k):
    count=defaultdict(int)
    left=ans=0
    for right in range(len(s)):
        count[s[right]]+=1
        while len(count) > k:
          print(count)
          count[s[left]] -= 1
          if count[s[left]] == 0:
            del count[s[left]]
          left += 1
    ans = max(ans, right - left + 1)
    return ans

print(find_longest_substring("eceba",2))
