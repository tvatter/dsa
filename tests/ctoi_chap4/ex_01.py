from itertools import chain
from queue import Queue
from typing import List


class Node:
  def __init__(self, key=None):
    self.key = key
    self.neighbors = []
    self.visited = False


class Graph:
  def __init__(self, nodes: List[Node] = None):
    self.nodes = nodes

  def reset_visited(self):
    for node in self.nodes:
      node.visited = False

  def from_adj_list(self, adj_list, directed=False):
    keys = set(chain(*adj_list))
    nodes = [Node(key=key) for key in keys]
    for edge in adj_list:
      nodes[edge[0]].neighbors.append(nodes[edge[1]])
      if not directed:
        nodes[edge[1]].neighbors.append(nodes[edge[0]])
    self.nodes = nodes

  def search(self, source, target):
    self.reset_visited()
    if source.key == target.key:
      return True

    queue = Queue()
    queue.put(source)
    while not queue.empty():
      current = queue.get()
      if current.key == target.key:
        return True
      current.visited = True
      for neighbor in current.neighbors:
        if not neighbor.visited:
          queue.put(neighbor)
    return False


adj_lst = [[0, 1], [0, 4], [0, 5], [1, 3], [1, 4], [2, 1], [3, 2], [3, 4]]
g = Graph()
g.from_adj_list(adj_lst, directed=True)
g.search(g.nodes[0], g.nodes[4])
g.search(g.nodes[4], g.nodes[0])

g.from_adj_list(adj_lst, directed=False)
g.search(g.nodes[0], g.nodes[4])
g.search(g.nodes[4], g.nodes[0])
