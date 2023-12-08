#!/bin/python3

import os
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#
sys.setrecursionlimit(8 * 1000)


class Node:

    def __init__(self, value):
        self.value = value
        self.neighbours = {}


class Graph:
    def __init__(self, count):
        self.node_map = {}
        for i in range(count + 1):
            self.node_map[i] = Node(value=i)

    def insert_edge(self, value1, value2):
        node1 = self.node_map[value1]
        node2 = self.node_map[value2]
        node1.neighbours[value2] = node2
        node2.neighbours[value1] = node1

    def get_forests(self):
        forests = []
        all_visited_keys = set()
        for key in self.node_map:
            if key in all_visited_keys:
                continue
            group = set()
            dfs(self.node_map[key], group)
            all_visited_keys.update(group)
            forests.append(group)
        return forests


def dfs(node, group):
    if node.value in group:
        return
    group.add(node.value)
    for key in node.neighbours:
        if key not in group:
            dfs(node.neighbours[key], group)
    return


def journey_to_the_moon(n, astronaut):
    graph = Graph(count=n)
    [graph.insert_edge(pair[0], pair[1]) for pair in astronaut]
    forests = graph.get_forests()
    group_choices = [len(group) for group in forests]
    sum_group_pairs = sum([(i * (i - 1) // 2) for i in group_choices])
    all_pairs = n * (n - 1) // 2
    return all_pairs - sum_group_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journey_to_the_moon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
