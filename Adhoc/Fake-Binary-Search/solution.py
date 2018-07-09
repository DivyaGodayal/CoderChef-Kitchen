if __name__ == '__main__':

    # Number of test cases.
    T = int(input())
    for i in range(T):

        # N - Number of elements in the array.
        # Q - Number of queries / elements to be searched for.
        (N, Q) = list(map(int, input().split()))

        # All the elements in the  array.
        nums = list(map(int, input().split()))

        # Sort the array
        sorted_nums = sorted(nums)

        # Dictionary to store the indices of elements in sorted array.
        sorted_index_map = {}

        # Dictionary to store the indices of elements in the original array.
        index_map = {}

        for ind in range(N):
            sorted_index_map[sorted_nums[ind]] = ind
            index_map[nums[ind]] = ind

        # Go through the array in the binary search fashion.
        for j in range(Q):
            # X is the element to be searched.
            X = int(input())

            # Index of X in original array.
            index_X = index_map[X]
            
            # Count of low and high meant to record the swaps needed to eventually make the correct move. 
            # for e.g. if the middle element needs to be swapped with an element lower than X we increase the lower count.
            count_low_needed = 0
            count_high_needed = 0
            
            # If the middle element is placed rightly we need to record the count.
            # This can then be used to calculate how many elements are left with which the swap can actually be done.
            correctly_placed_low = 0
            correctly_placed_high = 0
            
            total = 0

            # While doing the regular binary search we record a few counts.
            # These counts help us to find out the minimum number of swaps needed.
            low = 0
            high = N - 1
            
            while low <= high:
                # Middle element
                mid = int((low + high) / 2)

                # If we find the element then
                if nums[mid] == X:
                    break
                elif index_X > mid:
                    # If the index of X in the original array is greater than the current mid.
                    # this means our correct move should be going to the right.
                    # and thus we need to make changes accordingly so that we end up in the correct move.
                    if nums[mid] > X: 
                        # If the middle element is greater than X, it would make us go to the left.
                        # But we need to go right, so we record this as a swap needed with element lower than X.
                        count_low_needed += 1
                    else:
                        # If the middle element is lower than X, then its placed correctly and we record that too.
                        correctly_placed_low += 1
                    low = mid + 1
                else: 
                    # If the index of X in the original array is lesser than the current mid.
                    # this means our correct move should be going to the left.
                    # and thus we need to make changes accordingly so that we end up in the correct move.
                    if nums[mid] < X:
                        # If the middle element is lesser than X, it would make us go to the right.
                        # But we need to go left, so we record this as a swap needed with element higher than X.
                        count_high_needed += 1
                    else:
                        # If the middle element is greater than X, then its placed correctly and we record that too.
                        correctly_placed_high += 1
                    high = mid - 1
            
            if count_low_needed == 0 and count_high_needed == 0:
                # if there are no swap needed then return 0.
                total = 0
            else:
                # Total number of elements lower/higher than X which are available for a swap.
                # We use the sorted index to get the elements lower/higher than X.
                # and then subtract that by number of elements which are correctly placed as middle elements.
                total_lows = sorted_index_map[X] - correctly_placed_low
                total_highs = N - sorted_index_map[X] - 1 - correctly_placed_high
                
                # If the total number of lower/higher elements needed are greater than the available elements for swap.
                # Then we don't have enough elements for swap and we return -1.
                if count_low_needed - total_lows > 0 or count_high_needed - total_highs > 0:
                    total = -1
                else:     
                    # In the end we return the max of count of low needed or high needed since 
                    # min(count_low_needed, count_high_needed) elements could be swapped with each other 
                    # Which leaves us with the rest to be swapped. Hence the max would ensure we are including all the 
                    # necessary elements needed for swap.
                    total = max(count_low_needed, count_high_needed)
            print total