# from heapq import *
from itertools import chain
from typing import List

from dsa.data_structures.graph_node import GraphNode
from dsa.data_structures.heap import MinHeap
from dsa.data_structures.linked_list import LinkedList
from dsa.data_structures.queue import Queue

# from dsa.misc.class_generator import add_property, generate_class

# generate_class('Graph', 'src/dsa/data_structures/graph.py')
# add_property('Graph', 'src/dsa/data_structures/graph.py', 'nodes')


class Graph:
  """The Graph class"""
  def __init__(self, nodes: List[GraphNode] = None):
    if nodes is not None:
      self._nodes = {node.key: node for ix, node in enumerate(nodes)}
    else:
      self._nodes = None

  @property
  def nodes(self):
    return self._nodes

  @property
  def keys(self):
    return self._keys

  def from_adj_list(self, adj_list, directed=False):
    keys = set(chain(*adj_list))
    nodes = {key: GraphNode(key=key, children=[]) for key in keys}
    for edge in adj_list:
      nodes[edge[0]].children.append(nodes[edge[1]])
      if not directed:
        nodes[edge[1]].children.append(nodes[edge[0]])
    self._nodes = nodes

  # def dfs(self, root=None, reset_nodes=True, verbose=True):
  #   if reset_nodes:
  #     self._reset_nodes()
  #   if root is None:
  #     return
  #   if verbose:
  #     print(root)
  #   root.data['visited'] = True
  #   for child in root.children:
  #     if not child.data['visited']:
  #       self.dfs(child, reset_nodes=False)

  def dfs(self, nodes=None, reset_nodes=True, verbose=True):
    if reset_nodes:
      self._reset_nodes()
    if nodes is None:
      nodes = self.nodes.values()
    time = 0
    for node in nodes:
      if not node.data['visited']:
        time = self._dfs(node, time, verbose)

  def _reset_nodes(self, source=None):
    for node in self.nodes.values():
      node.data = {'visited': False, 'predecessor': None, 'meta': float('Inf')}
    if source is not None:
      source.data['meta'] = 0

  def _dfs(self, root, time, verbose=True):
    time = time + 1
    root.data['meta'] = {'s': time}
    root.data['visited'] = True
    if verbose:
      print('node {}, time d: {}'.format(root.key, time))
    for child in root.children:
      if not child.data['visited']:
        time = self._dfs(child, time, verbose)
    time = time + 1
    root.data['meta']['f'] = time
    if verbose:
      print('node {}, time f: {}'.format(root.key, time))
    return time

  def bfs(self, root=None, reset_nodes=True, verbose=True):
    if root is None:
      root = list(self._nodes.values())[0]
    if reset_nodes:
      self._reset_nodes(root)

    queue = Queue()
    queue.enqueue(root)
    while not queue.isempty():
      node = queue.dequeue()
      node.data['visited'] = True
      if verbose:
        print(node)
      for child in node.children:
        if not child.data['visited']:
          child.data['visited'] = True
          child.data['predecessor'] = node
          child.data['meta'] = node.data['meta'] + 1
          queue.enqueue(child)

  # Dumb implementation
  # O(V + E) + O(V log V)
  # One should save the order while doing the DFS to gain an O(V log V) term
  def topological_sort(self):
    self.dfs(verbose=False)
    for key, node in self._nodes.items():
      print([key, node.data['meta']['f']])
    nodes = sorted(self.nodes.values(),
                   key=lambda node: -node.data['meta']['f'])
    self._nodes = {node.key: node for node in nodes}
    print('---')
    for key, node in self._nodes.items():
      print([key, node.data['meta']['f']])

  # Note that, with the default weight, a BFS is more efficient...
  def djikstra(self, source, weight=lambda u, v: 1.0):
    self._reset_nodes(source)
    handles = list(self._nodes.keys())
    values = [node.data['meta'] for node in self._nodes.values()]
    queue = MinHeap(values, handles)
    while not queue.isempty():
      tmp = queue.pop()
      key = tmp[0]
      curr_weight = tmp[1]
      node = self._nodes[key]
      for child in node.children:
        tmp = curr_weight + weight(node, child)
        if child.data['meta'] > tmp:
          child.data['meta'] = tmp
          child.data['predecessor'] = node
          queue.update_value(queue.keys[child.key], tmp)

  # Alternative implementation which isn't exactly the CLRS / classical algo
  # For heap implementations that don't keep track (see CLRS Chapter 6.5)
  # def djikstra(self, source, weight=None):
  #   self._reset_nodes(source)
  #   queue = []
  #   heappush(queue, [0, source.key])
  #   while queue:
  #     tmp = heappop(queue)
  #     curr_weight = tmp[0]
  #     node = self._nodes[tmp[1]]
  #     for child in node.children:
  #       tmp = curr_weight + weight(node, child)
  #       if child.data['meta'] > tmp:
  #         child.data['meta'] = tmp
  #         child.data['predecessor'] = node
  #         heappush(queue, [tmp, child.key])
  # def djikstra(self, source, weight=lambda u, v: 1.0):
  #     self._reset_nodes(source)
  #     queue = MinHeap()
  #     queue.insert([0, source.key])
  #     while queue:
  #       tmp = queue.pop()
  #       curr_weight = tmp[0]
  #       key = tmp[1]
  #       node = self._nodes[key]
  #       for child in node.children:
  #         tmp = curr_weight + weight(node, child)
  #         if child.data['meta'] > tmp:
  #           child.data['meta'] = tmp
  #           child.data['predecessor'] = node
  #           queue.insert([tmp, child.key])

  def mst_prim(self, weight):
    self._reset_nodes()
    handles = list(self._nodes.keys())
    values = [float('inf')] * len(self._nodes)
    queue = MinHeap(values, handles)
    while not queue.isempty():
      tmp = queue.pop()
      node = self._nodes[tmp[0]]
      node.data['visited'] = True
      for child in node.children:
        # import pdb
        # pdb.set_trace()
        tmp = weight(node, child)
        if not child.data['visited'] and child.data['meta'] > tmp:
          child.data['meta'] = tmp
          child.data['predecessor'] = node
          queue.update_value(queue.keys[child.key], tmp)
    adj_list = []
    for key, node in self._nodes.items():
      if node.data['predecessor'] is not None:
        adj_list.append(sorted([key, node.data['predecessor'].key]))
    return adj_list

  def print_path(self, source, target, reset_nodes=True):
    if reset_nodes:
      self.bfs(source, verbose=False)
    if source.key == target.key:
      print(source)
    elif target.data['predecessor'] is None:
      print('No path from source to target exists.')
    else:
      self.print_path(source, target.data['predecessor'])
      print(target)


if __name__ == '__main__':

  # Adj list from CTOI
  adj_lst = [[0, 1], [0, 4], [0, 5], [1, 3], [1, 4], [2, 1], [3, 2], [3, 4]]
  g = Graph()
  g.from_adj_list(adj_lst)
  g.dfs()
  g.dfs(nodes=[g.nodes[3], g.nodes[5]])
  g.bfs(g.nodes[0])

  g.print_path(g.nodes[0], g.nodes[3])
  g.print_path(g.nodes[0], g.nodes[4], reset_nodes=False)
  g.print_path(g.nodes[4], g.nodes[0])

  g.topological_sort()

  g = Graph()
  weight1 = lambda u, v: 1.0
  weight2 = lambda u, v: (u.key - v.key)**2
  from inspect import getsource
  from itertools import product
  print({'adj_list': adj_lst})
  for directed, weight in product([True, False], [weight1, weight2]):
    print({'directed': directed, 'weight': getsource(weight)})
    g.from_adj_list(adj_lst, directed=directed)
    g.djikstra(g.nodes[0], weight=weight)
    print([[node.key, node.data['meta']] for node in g.nodes.values()])

    g.djikstra(g.nodes[1], weight=weight)
    print([[node.key, node.data['meta']] for node in g.nodes.values()])

  # Adf list from CLRS
  adj_lst = [['a', 'b'], ['a', 'h'], ['b', 'h'], ['b', 'c'], ['h', 'i'],
             ['g', 'h'], ['c', 'i'], ['g', 'i'], ['c', 'd'], ['c', 'f'],
             ['f', 'g'], ['d', 'f'], ['d', 'e'], ['e', 'f']]
  weights = [4, 8, 11, 8, 7, 1, 2, 6, 7, 4, 2, 14, 9, 10]
  weight = lambda u, v: weights[adj_lst.index(sorted([u.key, v.key]))]
  g = Graph()
  g.from_adj_list(adj_lst)
  print(g.mst_prim(weight))
