class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        prev_time, fleets = 0, 0
        for p, s in cars:
            t = (target - p) / s
            if t > prev_time:
                fleets += 1
                prev_time = t
        
        return fleets