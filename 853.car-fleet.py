class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = list(zip(position, speed))
        ps.sort(reverse=True)


        # Ascending list of a fleet's time taken to reach their destination
        fleet_stack = []
        for p, s in ps:
            distance_taken = (target - p ) / s
            if fleet_stack and fleet_stack[-1] >= distance_taken:
                continue
            fleet_stack.append(distance_taken)
        return len(fleet_stack)