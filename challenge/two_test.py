from two import *
import unittest


class TestTwo(unittest.TestCase):
    def test_init(self):
        n1 = Node("sea")
        n2 = Node("shore")
        l1 = Link(n1,n2)
        n1.add_pointer(l1)
        fl = n1.find_link(n2)
        assert l1.weight == 0
        assert fl == 0

if __name__ == '__main__':
    unittest.main()
