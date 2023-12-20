import re
from typing import List

# A polygon class with integer vertices
class Polygon():
    def __init__(self, vertices: List[List[int]]):
        self.vertices = vertices
        self.edges = []
        for i in range(len(vertices)):
            self.edges.append([vertices[i], vertices[(i + 1) % len(vertices)]])

    # get the area of the polygon using triangle method
    def getArea(self):
        result = 0
        for i in range(len(self.vertices)):
            j = (i + 1) % len(self.vertices)
            result += self.vertices[i][0] * self.vertices[j][1] - self.vertices[j][0] * self.vertices[i][1]
        return abs(result) / 2 + self.getPerimeter()

    #get the length of the perimeter of the polygon
    def getPerimeter(self):
        result = 0
        for i in range(len(self.vertices)):
            j = (i + 1) % len(self.vertices)
            result += ((self.vertices[i][0] - self.vertices[j][0]) ** 2 + (self.vertices[i][1] - self.vertices[j][1]) ** 2) ** 0.5
        return result


with open("input.txt", "r") as test:
    startPoint = [0, 0]
    vertices = [startPoint]
    directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
    for line in [x.strip() for x in test.readlines()]:
        match = re.match(r"([UDLR]) (\d+) \(#([0-9a-f]{6})\)", line)
        color = match.group(3)
        # Interpret first five characters of color as hex number
        distance = int(color[:5], 16)
        direction = directions[int(color[5])]
        endPoint = [startPoint[0] + distance * direction[0], startPoint[1] + distance * direction[1]]
        vertices.append(endPoint)
        startPoint = endPoint

    P = Polygon(vertices)
    print(P.getArea() - P.getPerimeter() / 2 + 1) # Picks theorem: A = I + B / 2 - 1