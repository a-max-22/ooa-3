import unittest
from  Box import  Point, Dimensions, Box
from Element import Element, VoidElem


class TestBox(unittest.TestCase):
    def test_create(self):
        width, height = 2,3 
        d = Dimensions(width, height)
        b = Box(d, None)
        
        self.assertEqual(b.get_set_cell_status(), b.SET_CELL_NIL)


    def test_get_cell(self):
        d = Dimensions(width = 2, height = 3)
        p1 = Point(x = 1, y = 2)
        p2 = Point(x = 0, y = 0)

        b = Box(d)
        cell = b.get_cell(p1)
        self.assertNotEqual(cell, VoidElem)

        cell = b.get_cell(p2)
        self.assertNotEqual(cell, VoidElem)


    def test_get_cell_out_of_bounds(self):
        d = Dimensions(width = 2, height = 3)
        p1 = Point(x = 2, y = 3)
        p2 = Point(x = -1, y = -1)
        p3 = Point(x = 2, y = 1)

        b = Box(d)
        
        cell = b.get_cell(p1)
        self.assertEqual(cell, VoidElem)

        cell = b.get_cell(p2)
        self.assertEqual(cell, VoidElem)

        cell = b.get_cell(p3)
        self.assertEqual(cell, VoidElem)


    def test_set_cell(self):
        d = Dimensions(width = 2, height = 3)
        p = Point(x = 1, y = 2)

        b = Box(d)
        elem = Element()
        b.set_cell(p, elem)

        self.assertEqual(b.get_set_cell_status(), b.SET_CELL_OK)

        elem_in_box = b.get_cell(p)
        self.assertEqual(elem_in_box, elem)



    def test_set_cell_out_bounds(self):
        d = Dimensions(width = 2, height = 3)
        p = Point(x = 2, y = 1)

        b = Box(d)
        elem = Element()
        b.set_cell(p, elem)

        self.assertEqual(b.get_set_cell_status(), b.SET_CELL_ERR)

        elem_in_box = b.get_cell(p)
        self.assertEqual(elem_in_box, VoidElem)

