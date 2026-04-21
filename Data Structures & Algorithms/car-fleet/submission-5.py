class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort(reverse=True)

        times = []
        for car in cars:
            dist = target - (car[0])
            times.append(dist/car[1])

        min_time, res = times[0], 1
        for t in times:
            if t > min_time:
                res += 1
                min_time = t
        
        return res