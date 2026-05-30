class MinStack:

    def __init__(self):
        self.l = []
        self.mini = []

    def push(self, val: int) -> None:
        self.l.append(val)

        if not self.mini:
            self.mini.append(val)
        else:
            self.mini.append(
                min(val, self.mini[-1])
            )

    def pop(self) -> None:
        self.l.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.mini[-1]
