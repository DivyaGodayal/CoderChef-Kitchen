from collections import Counter
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        num_dict = {}
        ans_dict = {}

        # Frequency dictionary for the number array.
        num_dict = Counter(nums)

        # REDUCTION STEP
        reduced_list = []
        reduced_dict = {}
        index = 0

        for key in num_dict:

            # 3 is the maximum frequency we need for an element
            min_ = min(3, num_dict[key])
            reduced_list.extend([key]*min_)

            # Dictionary is used to keep track of the of reduced elements
            reduced_dict[key] = min_

        # Iterate over the reduced list to get the unique 3 sum triplets
        for i in range(len(reduced_list)-1):
            for j in range(i+1, len(reduced_list)):
                # first element
                first_num = reduced_list[i]
                # second element
                second_num = reduced_list[j]
                # remaining sum - deciding the third element
                remaining_sum = (first_num + second_num) * -1

                # If the remaining element is one of the elements in the reduced list.
                if remaining_sum in reduced_dict:
                    # count of similar elements in the tuple
                    match_count = ((remaining_sum == first_num) + (remaining_sum == second_num)) + 1

                    # If there are not enough elements in the given list to form the tuple
                    if reduced_dict[remaining_sum] < match_count:
                        continue

                    # Otherwise add the unique tuple to the ans tuple dictionary
                    tuple_ = tuple(sorted((first_num, second_num, remaining_sum)))
                    if tuple_ not in ans_dict:
                        ans_dict[tuple_] = True

        return ans_dict.keys()
