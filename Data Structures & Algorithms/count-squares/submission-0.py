class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        x, y = point

        if (x, y) not in self.points:
            self.points[(x, y)] = 0

        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0

        # Try every point as the horizontally opposite corner
        for (x2, y2), count in self.points.items():

            # Must be on the same horizontal line
            if y2 != y:
                continue

            # Cannot be the same point
            if x2 == x:
                continue

            d = abs(x2 - x)

            # Square above
            ans += (
                count
                * self.points.get((x, y + d), 0)
                * self.points.get((x2, y + d), 0)
            )

            # Square below
            ans += (
                count
                * self.points.get((x, y - d), 0)
                * self.points.get((x2, y - d), 0)
            )

        return ans