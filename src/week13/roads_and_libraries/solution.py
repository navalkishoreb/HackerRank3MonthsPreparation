#!/bin/python3

import os


#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

class Node:
    def __init__(self, value, neighbours=None):
        self.neighbours = set() if neighbours is None else neighbours
        self.value = value


class Graph:

    def __init__(self, nodes):
        self.node_map = {}
        for i in range(1, nodes + 1):
            self.node_map[i] = Node(value=i)

    def insert_edge(self, value_a, value_b):
        node_a = self.node_map[value_a]
        node_b = self.node_map[value_b]
        self.node_map[value_a].neighbours.add(node_b)
        self.node_map[value_b].neighbours.add(node_a)


def populate_graph_with_edges(graph, cities):
    for item in cities:
        node_a = item[0]
        node_b = item[1]
        graph.insert_edge(value_a=node_a, value_b=node_b)


def dfs(node, visited):
    if node.value in visited:
        return
    visited.add(node.value)
    for node in node.neighbours:
        if node.value not in visited:
            dfs(node=node, visited=visited)


def find_disjoint_nodes(full_graph: Graph):
    groups = []
    all_visited_node = set()
    for key in full_graph.node_map:
        if key in all_visited_node:
            continue
        group_visited_node = set()
        dfs(node=full_graph.node_map[key], visited=group_visited_node)
        groups.append(group_visited_node)
        all_visited_node.update(group_visited_node)
    return groups


def roads_and_libraries(n, c_lib, c_road, cities):
    graph = Graph(n)
    populate_graph_with_edges(graph=graph, cities=cities)
    forests = find_disjoint_nodes(graph)
    all_libraries_cost = len(forests) * c_lib
    all_roads_cost = sum([len(item) - 1 for item in forests]) * c_road
    libraries_with_road = all_libraries_cost + all_roads_cost
    only_libraries_without_road = n * c_lib

    return min(only_libraries_without_road, libraries_with_road)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roads_and_libraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
