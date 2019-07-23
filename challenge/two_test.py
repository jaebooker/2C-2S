from two import *
import unittest


class TestTwo(unittest.TestCase):
    def test_init(self):
        n1 = Node("sea")
        n2 = Node("shore")
        l1 = Link(n1,n2)
        n1.add_pointer(l1)
        fl = n1.find_link(n2)
        nodes = Nodes([n1,n2])
        nbfs = bfs(nodes, n1.data)
        path = bfs_paths(nodes, n1.data, n2.data)
        assert l1.weight == 0
        assert fl == 0
        assert nbfs == set(["shore","sea"])
        assert list(path) == [['sea','shore']]

    def test_shortest_path(self):
        n1 = Node("sea")
        n2 = Node("shore")
        n3 = Node("she")
        n4 = Node("sells")
        l1 = Link(n1,n2)
        l2 = Link(n1,n3)
        l3 = Link(n3,n4)
        l4 = Link(n4,n2)
        n1.add_pointer(l1)
        n1.add_pointer(l2)
        n3.add_pointer(l3)
        n4.add_pointer(l4)
        fl = n1.find_link(n2)
        nodes = Nodes([n1,n2,n3,n4])
        nbfs = bfs(nodes, n1.data)
        path = bfs_paths(nodes, n1.data, n2.data)
        short_path = shortest_path(nodes, n1.data, n2.data)
        assert short_path == ['sea','shore']

if __name__ == '__main__':
    unittest.main()
