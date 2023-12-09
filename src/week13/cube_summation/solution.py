#!/bin/python3

import os


#
# Complete the 'cubeSum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY operations
#

class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def is_in_between(self, first, second):
        return (first.x <= self.x <= second.x or second.x <= self.x <= first.x) and (
                first.y <= self.y <= second.y or second.y <= self.y <= first.y) and (
                first.z <= self.z <= second.z or second.z <= self.z <= first.z)

    def is_valid(self, cube_size):
        return 0 < self.x <= cube_size and 0 < self.y <= cube_size and 0 < self.z <= cube_size

    def __repr__(self):
        return f"({self.x, self.y, self.z})"


class Cube:

    def __init__(self, cube_size):
        self.cube_size = cube_size
        self.grid = {}

    def operate(self, operation):
        operation = operation.split()
        opcode = operation[0]
        options = list(map(int, operation[1:]))
        result = None
        if opcode == "UPDATE":
            x, y, z, value = options
            self.update(x=x, y=y, z=z, value=value)
        elif opcode == "QUERY":
            x1, y1, z1, x2, y2, z2 = options
            result = self.query(x1=x1, y1=y1, z1=z1, x2=x2, y2=y2, z2=z2)
        return result

    def update(self, x, y, z, value):
        coordinate = Coordinate(x=x, y=y, z=z)
        if coordinate.is_valid(cube_size=self.cube_size):
            self.grid[coordinate] = value

    def query(self, x1, y1, z1, x2, y2, z2):
        first = Coordinate(x=x1, y=y1, z=z1)
        second = Coordinate(x=x2, y=y2, z=z2)
        summation = 0
        for coordinate, value in self.grid.items():
            if coordinate.is_in_between(first=first, second=second):
                summation += value

        return summation


def cube_sum(n, operations):
    cube = Cube(cube_size=n)
    results = []
    for op in operations:
        result = cube.operate(operation=op)
        if result is not None:
            results.append(result)
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        first_multiple_input = input().rstrip().split()

        matSize = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        ops = []

        for _ in range(m):
            ops_item = input()
            ops.append(ops_item)

        res = cube_sum(matSize, ops)

        fptr.write('\n'.join(map(str, res)))
        fptr.write('\n')

    fptr.close()
