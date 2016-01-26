import unittest
"""
Python code that creates dictionaries corresponding to some simple examples of graphs,
along with two short functions that compute information
about the distribution of the in-degrees for nodes in these graphs
"""

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





class TestGraphMethods(unittest.TestCase):

  def test_make_complete_graph(self):
      self.assertEqual(make_complete_graph(1), {0:set([])})
      self.assertEqual(make_complete_graph(2), {0:set([1]), 1:set([0])})




if __name__ == '__main__':
    unittest.main()