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

    def test_length(self):
        vt = Vertex(1, "sea")
        vt2 = Vertex(2, "shore")
        vt.add_neighbor(vt2)
        g = Graph()
        g.add_vertex(vt)
        g.add_vertex(vt2)
        g.add_edge(vt, vt2)
        num_v = g.get_num_vertices()
        num_e = g.get_num_edges()
        assert num_v == 2
        assert num_e == 1


if __name__ == '__main__':
    unittest.main()
