from three import *
import unittest


class TestThree(unittest.TestCase):

    def test_dfs_path(self):
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
        ndfs = dfs_r(nodes, n1.data)
        ndfsi = dfs_i(nodes, n1.data)
        assert ndfs == set(["shore","sells","sea","she"])
        assert ndfsi == set(['shore','sells','she','sea'])

if __name__ == '__main__':
    unittest.main()
