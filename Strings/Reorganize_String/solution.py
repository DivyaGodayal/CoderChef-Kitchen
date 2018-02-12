from collections import Counter
import heapq
class Solution:
  def reorganizeString(self, S):
    res = ""
  pq = []
    c = Counter(S)
    for key, value in c.items():
      heapq.heappush(pq, (-value, key))
      prev_freq, prev_char = 0, ''
      while pq:
      freq, character = heapq.heappop(pq)
      res += character
      if prev_freq < 0:
      heapq.heappush(pq, (prev_freq, prev_char))
      freq += 1
      prev_freq, prev_char = freq, character

      if len(res) != len(S): return ""
                             return res
