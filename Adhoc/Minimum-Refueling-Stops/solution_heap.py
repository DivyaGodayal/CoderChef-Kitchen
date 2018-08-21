class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        
        # If there is no start fuel then return -1, since no station could be reached.
        if not startFuel:
            return -1
        
        min_refueling_stops = -1
        
        # Put the starting fuel in the heap.
        fuel_heap = [-startFuel]
        # Variable to count the number of stations.
        station_count = 0
        # Variable to keep a track of the current fuel.
        current_fuel = 0
        # While you exhaust all the stations.
        while fuel_heap:
            # Keep using the fuel from the heap.
            current_fuel += -heapq.heappop(fuel_heap)
            # Increase the count of stations used for re-fueling by 1, each time you pop.
            min_refueling_stops += 1
            # If at any point current fuel which you have is able to reach the target then return the ans.
            if current_fuel >= target:
                return min_refueling_stops
            # With the current fuel you can reach a station which is current_fuel miles away.
            # Push the fuels of all the stations which come on the way.
            # This would help to maintain a track of all the stations which could be used for refueling.
            while station_count < len(stations) and current_fuel >= stations[station_count][0]:
                heapq.heappush(fuel_heap, -stations[station_count][1])
                station_count += 1
                
        return -1
            