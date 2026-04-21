class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        times = []
        for car in cars:
            dist = target - (car[0])
            times.append(dist/car[1])

        prev_time, fleets = 0, 0
        for t in times:
            if t > prev_time:
                fleets += 1
                prev_time = t
        
        return fleets