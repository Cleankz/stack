import unittest
import random
from stac import Stack
from stac import balans

class DivTests(unittest.TestCase):
    def test_push(self):
        s = Stack()
        for i in range(100000):
            s.push(i)
        self.assertEqual(100000,s.size())
    def test_pop(self):
        s = Stack()
        for i in range(100):
            s.push(i)
        for j in range(101):
            s.pop()
        self.assertEqual(0,s.size())
    def test_peek(self):
        s = Stack()
        for i in range(100):
            s.push(i)
        for i in range(100):
            self.assertEqual(s.peek(),0)
    def test_size(self):
        s = Stack()
        for i in range(100):
            s.push(i)
        self.assertEqual(s.size(),100)
if __name__ == '__main__':
    unittest.main()