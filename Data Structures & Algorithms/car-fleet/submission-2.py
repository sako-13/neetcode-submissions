class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for index in range(len(position)):
            cars.append([position[index],speed[index]])
        cars.sort()
        timeneeded = []
        for index, car in enumerate(cars):
            timeneeded.append((target-car[0]) / car[1])
        fleets = 0
        fleet_time = 0
        while timeneeded:
            current_time = timeneeded.pop()
            if current_time > fleet_time:
                fleets += 1
                fleet_time = current_time
        return fleets
