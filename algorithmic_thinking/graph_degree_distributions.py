import unittest
"""
Python code that creates dictionaries corresponding to some simple examples of graphs,
along with two short functions that compute information
about the distribution of the in-degrees for nodes in these graphs
"""
#sample graphs
EX_GRAPH0 = {0:set([1, 2]),1:set([]), 2:set([])}
EX_GRAPH1 = {0:set([1, 4, 5]),1:set([2, 6]),2:set([3]),3:set([0]),
             4:set([1]),5:set([2]),6:set([])}
EX_GRAPH2 = {0:set([1, 4, 5]),1:set([2, 6]),2:set([7, 3]),3:set([7]),
             4:set([1]),5:set([2]),6:set([]),7:set([3]),
             8:set([1, 2]),9:set([0, 3, 4, 5, 6, 7])}

def make_complete_graph(num_nodes):
    #returns a dictionary representation of a complete graph
    #with the given number of nodes
    counter = 0
    node_dict = {}
    while counter < num_nodes:
        #get all nodes != current node
        node_list = [node for node in range(num_nodes) if node != counter]
        node_dict[counter] = set(node_list)
        counter += 1
    return node_dict

def compute_in_degrees(digraph):
    #Takes a directed graph digraph (represented as a dictionary) and computes
    #the in-degrees for the nodes in the graph. The function should return a dictionary with
    #the same set of keys (nodes) as digraph
    #whose corresponding values are the number of edges whose head matches a particular node.

    #create a list of the nodes that appear as values in the given digraph
    node_list = generate_head_nodes_list(digraph)
    #count the number of times each number appears in the list
    degrees = dict.fromkeys(digraph)
    for key, val in degrees.items():
        degrees[key] = node_list.count(key)
    return degrees

def generate_head_nodes_list(digraph):
    edges_head_list = []
    for key, val in digraph.items():
        if val:
           for item in val:
               edges_head_list.append(item)
    return edges_head_list


class TestGraphMethods(unittest.TestCase):


  def test_make_complete_graph(self):
      self.assertEqual(make_complete_graph(1), {0:set([])})
      self.assertEqual(make_complete_graph(2), {0:set([1]), 1:set([0])})
      self.assertEqual(make_complete_graph(4), {0:set([1, 2, 3]), 1:set([0, 2, 3]),
        2:set([0, 1, 3]), 3:set([0, 1, 2])})

  def test_gen_head_nodes(self):
      GRAPH0 = {0: set([1]),
          1: set([2]),
          2: set([3]),
          3: set([0])}
      self.assertEqual(generate_head_nodes_list(EX_GRAPH0), [1, 2])
      self.assertEqual(generate_head_nodes_list(GRAPH0), [1, 2, 3, 0])


  def test_compute_in_degree(self):
      # digraph = {}
      # self.assertEqual(compute_in_degrees(digraph), )
      GRAPH0 = {0: set([1]),
          1: set([2]),
          2: set([3]),
          3: set([0])}
      self.assertEqual(compute_in_degrees(GRAPH0), {0: 1, 1: 1, 2: 1, 3: 1})

if __name__ == '__main__':
    unittest.main()