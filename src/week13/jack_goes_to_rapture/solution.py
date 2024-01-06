#!/bin/python3
import heapq
import sys

sys.setrecursionlimit(8 * 1000)


#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

class MinHeapItem:

    def __init__(self, node, weight):
        self.node = node
        self.weight = weight

    def __eq__(self, other):
        if isinstance(other, MinHeapItem):
            return self.weight == other.weight

    def __lt__(self, other):
        if isinstance(other, MinHeapItem):
            return self.weight < other.weight

    def __repr__(self):
        return f"node={self.node}, weight={self.weight}"


class Node:

    def __init__(self, value):
        self.value = value
        self.neighbours = {}

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"{self.value}"

    def add_edge(self, to_node, weight: int):
        self.neighbours[to_node] = weight


def dfs(graph, visited, priority_heap, target_node, current_cost):
    if not priority_heap:
        return "NO PATH EXISTS"
    heap_item: MinHeapItem = heapq.heappop(priority_heap)
    current_node = heap_item.node
    current_cost = heap_item.weight
    if current_node == target_node:
        return current_cost
    if current_node in visited:
        # while current_node not in visited and priority_heap:
        #     heap_item: MinHeapItem = heapq.heappop(priority_heap)
        #     current_node = heap_item.node
        #     current_cost = heap_item.weight
        # heapq.heappush(priority_heap, MinHeapItem(node=current_node, weight=max(current_cost, current_cost)))
        return dfs(graph=graph, visited=visited, priority_heap=priority_heap, target_node=target_node,
                   current_cost=current_cost)

    visited.add(current_node)
    # print(current_node, current_cost)
    for node, weight in current_node.neighbours.items():
        if node not in visited:
            min_heap_item = MinHeapItem(node=node, weight=max(current_cost, weight))
            # print(f"{current_node}-->{node} = max({weight =!r}, {current_cost =!r}) :: {min_heap_item}")
            heapq.heappush(priority_heap, min_heap_item)
    return dfs(graph=graph, visited=visited, priority_heap=priority_heap, target_node=target_node,
               current_cost=current_cost)


class Graph:

    def __init__(self, node_count):
        self.node_map = {}
        for i in range(1, node_count + 1):
            self.node_map[i] = Node(value=i)

    def add_edge(self, from_node, to_node, weight):
        from_node_object = self.node_map[from_node]
        to_node_object = self.node_map[to_node]
        from_node_object.add_edge(to_node=to_node_object, weight=weight)
        to_node_object.add_edge(to_node=from_node_object, weight=weight)

    def get_minimum_cost(self, start, end):
        start_item = MinHeapItem(node=self.node_map[start], weight=0)
        priority_heap = [start_item]
        return dfs(graph=self, visited=set(), priority_heap=priority_heap, target_node=self.node_map[end],
                   current_cost=0)


# def get_cost(g_nodes, g_from, g_to, g_weight):
#     graph = Graph(node_count=g_nodes)
#     for from_node, to_node, weight in zip(g_from, g_to, g_weight):
#         graph.add_edge(from_node, to_node, weight)
#
#     return graph.get_minimum_cost(start=1, end=g_nodes)


def get_cost(g_nodes, g_from, g_to, g_weight):
    G = [[] for i in range(g_nodes + 1)]
    for from_node, to_node, weight in zip(g_from, g_to, g_weight):
        G[from_node].append((to_node, weight))
        G[to_node].append((from_node, weight))

    current_cost = 0
    current_node = 1
    active = [(current_cost, current_node)]
    out = 'NO PATH EXISTS'
    visited = [False] * (g_nodes + 1)
    while len(active):
        current_cost, current_node = heapq.heappop(active)
        if visited[current_node]: continue
        visited[current_node] = True
        if current_node == g_nodes:
            out = current_cost
            break
        for neighbour, weight in G[current_node]:
            if not visited[neighbour]:
                heapq.heappush(active, (max(current_cost, weight), neighbour))
    return out


if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    result = get_cost(g_nodes, g_from, g_to, g_weight)
    print(result)
