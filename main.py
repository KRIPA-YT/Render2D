from turtle import *
from math import *


def checkTuple(t, name):
    if type(t) != tuple:
        raise ValueError(name + " must be a 2D Tuple")

    if len(t) != 2:
        raise ValueError(name + "coord must be a 2D Tuple")


def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point
    angle = radians(-angle)

    qx = ox + cos(angle) * (px - ox) - sin(angle) * (py - oy)
    qy = oy + sin(angle) * (px - ox) + cos(angle) * (py - oy)
    return qx, qy


class Render2D:
    __instructionSet = []

    class Instruction:
        __coordinateSet = []

        penColor = ''
        fillColor = ''

        def __init__(self, penColor='black', fillColor=''):
            self.penColor = penColor
            self.fillColor = fillColor

        def addCoordinate(self, coord):
            checkTuple(coord, 'coord')
            self.__coordinateSet.append(coord)

        def getCoordinateSet(self):
            return self.__coordinateSet

    def __init__(self, origin=(0, 0)):
        self.__origin = origin

    def addInstruction(self, instruction):
        self.__instructionSet.append(instruction)
        return self

    def __generateInstruction(self, coordSet, rotation, penColor, fillColor, add=True):
        ins = self.Instruction(penColor, fillColor)
        rotation = radians(-rotation)

        # Rotate Coordinates
        for coord in coordSet:
            ins.addCoordinate(rotate(self.getOrigin(), coord, rotation))

        if add:
            self.addInstruction(ins)

        return ins

    def getInstruction(self, index):
        return self.__instructionSet[index]

    def getInstructionSet(self):
        return self.__instructionSet

    def setOrigin(self, origin):
        checkTuple(origin, 'origin')
        self.__origin = origin

    def getOrigin(self):
        return self.__origin

    def square(self, mid, sideLength, rotation=0, penColor='black', fillColor=''):
        diagonal = sqrt(2 * pow(sideLength / 2, 2))
        coordSet = []
        corner = mid[0] + diagonal
        for angle in range(45, 360 + 90 + 45, 90):
            coordSet.append(rotate(mid, (corner, mid[1]), angle))

        self.__generateInstruction(coordSet, rotation, penColor, fillColor)
        return self


def main():
    renderer = Render2D()
    renderer.square((0, 0), 100)
    instruction = renderer.getInstructionSet()[0]
    print(instruction.getCoordinateSet())

    t = Turtle()
    t.penup()
    for coord in instruction.getCoordinateSet():
        t.goto(coord)
        t.pendown()
    done()


if __name__ == '__main__':
    main()
