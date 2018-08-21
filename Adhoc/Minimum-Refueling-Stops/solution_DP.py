class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        # DP array to save whats the maximum reach for a number of stations.
        dp = [startFuel] + [0] * len(stations)
        # Enumerate each station one by one.
        for i, (loc, fuel) in enumerate(stations):
            # Get the maximum reach of all stations behind it.
            for j in range(i, -1, -1):
                # If the maximum reach of the station behind is greater than the current stations location.
                # This means we can add up current stations fuel and see whats the updated reach with one extra fuel stop.
                if dp[j] >= loc:
                    # We keep storing the maximum possible reach corresponding to any station.
                    dp[j+1] = max(dp[j+1], dp[j] + fuel) 
           
        # If in the DP array there is a element which has DP[i] = target
        # That means it will take i stations to reach the target.
        for i, d in enumerate(dp):
            if d >= target: return i
        return -1