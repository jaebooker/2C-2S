from one import *
import unittest


class TestOne(unittest.TestCase):
    def test_init(self):
        vt = Vertex(1, "sea")
        vt2 = Vertex(2, "shore")
        vt.add_neighbor(vt2)
        vtn = vt.get_neighbors()
        vtne = vt.get_edge_weight(vt2)
        assert len(vt.neighbors) == 1
        assert vt.id == 1
        assert vt.data == "sea"
        assert len(vtn) == 1
        assert vtne == 0

if __name__ == '__main__':
    unittest.main()
