#!/usr/bin/python
# -*- coding: utf-8 -*-

import heapq
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        freq = Counter(tasks)

        heaplist = [(-freq[key], key) for key in freq]
        heapq.heapify(heaplist)

        interim_list = []
        steps = 0
        is_non_zero = False

        while heaplist:
            i = 0

            while i <= n:
                if heaplist:
                    (frequency, character) = heapq.heappop(heaplist)
                    if frequency + 1 < 0:
                        is_non_zero = True
                    interim_list.append((frequency + 1, character))
                else:
                    break
                i += 1
            steps += (n + 1 if is_non_zero else i)

            for element in interim_list:
                if element[0] < 0:
                    heapq.heappush(heaplist, element)
            interim_list = []
            is_non_zero = False
        return steps



