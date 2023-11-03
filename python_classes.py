class Point:
    def __init__(self, xCoord: float, yCoord: float) -> None:
        self.xCoord = xCoord
        self.yCoord = yCoord
    
    def getCoordinates(self) -> str:
        return f"{{x: {self.xCoord}, y: {self.yCoord}}}"


point = Point(2, 5)
print(point.getCoordinates())