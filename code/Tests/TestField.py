import unittest
from  Field import Field, create_field, Point, Dimensions
from Element import Element


class TestFieldCreate(unittest.TestCase):
    def test_create_invalid_field(self):
        status, _ = create_field(-1,-1)
        
        self.assertEqual(status, Field.CREATE_ERR)

    def test_create_field(self):
        status, _ = create_field(1,1)
        self.assertEqual(status, Field.CREATE_OK)


class TestFieldQueryCell(unittest.TestCase):
    def test_query_cell_empty(self):
        w,h = 2, 2
        p = Point(w - 1, h - 1)

        _, field = create_field(w, h)
        self.assertEqual(field.get_query_cell_status(), Field.QRY_CELL_NIL)

        field.query_cell(p)
        self.assertEqual(field.get_query_cell_status(), Field.QRY_CELL_OK)
        self.assertTrue(field.is_cell_empty())


    def test_query_cell_nonempty(self):
        w,h = 2, 3
        p = Point(1, 2)

        _, field = create_field(w,h)
        self.assertEqual(field.get_query_cell_status(), Field.QRY_CELL_NIL)

        field.set_cell_content(p, Element())

        field.query_cell(p)
        self.assertEqual(field.get_query_cell_status(), Field.QRY_CELL_OK)
        self.assertFalse(field.is_cell_empty())


    def test_query_cell_out_of_bounds(self):
        w, h = 2, 2
        p = Point(w + 1, h + 1)

        _, field = create_field(w, h)

        field.query_cell(p)
        self.assertEqual(field.get_query_cell_status(), Field.QRY_CELL_ERR)



class TestFieldSetCell(unittest.TestCase):
    def test_set_cell(self):
        w,h = 2, 2
        p = Point(w - 1, h - 1)

        _, field = create_field(w, h)
        self.assertEqual(field.get_set_cell_content_status(), Field.SET_CELL_NIL)

        elem = Element()
        field.set_cell_content(p, elem)

        self.assertEqual(field.get_set_cell_content_status(), Field.SET_CELL_OK)


    def test_set_cell_nonempty(self):
        w,h = 2, 2
        p = Point(w - 1, h - 1)

        _, field = create_field(w, h)
        self.assertEqual(field.get_set_cell_content_status(), Field.SET_CELL_NIL)

        elem1 = Element()
        elem2 = Element()

        field.set_cell_content(p, elem1)
        self.assertEqual(field.get_set_cell_content_status(), Field.SET_CELL_OK)

        field.set_cell_content(p, elem2)
        self.assertEqual(field.get_set_cell_content_status(), Field.SET_CELL_ERR)


    def test_set_cell_out_of_bounds(self):
        w,h = 2, 2
        p1 = Point(w + 1, h + 1)
        p2 = Point(-w, -h)

        _, field = create_field(w,h)

        field.set_cell_content(p1, Element())
        self.assertEqual(field.get_set_cell_content_status(), Field.SET_CELL_ERR)

        field.set_cell_content(p2, Element())
        self.assertEqual(field.get_set_cell_content_status(), Field.SET_CELL_ERR)



class TestFieldGetCell(unittest.TestCase):
    def test_get_cell_empty(self):
        w,h = 2, 2
        p = Point(w - 1, h - 1)

        _, field = create_field(w, h)
        self.assertEqual(field.get_get_cell_content_status(), Field.GET_CELL_NIL)

        field.get_cell_content(p)

        self.assertEqual(field.get_get_cell_content_status(), Field.GET_CELL_ERR)

    def test_get_cell_nonempty(self):
        w,h = 2, 2
        p = Point(w - 1, h - 1)

        _, field = create_field(w, h)
        self.assertEqual(field.get_get_cell_content_status(), Field.GET_CELL_NIL)

        elem = Element()
        field.set_cell_content(p, elem)
        field.get_cell_content(p)

        self.assertEqual(field.get_get_cell_content_status(), Field.GET_CELL_OK)
        self.assertEqual(field.get_get_cell_content_result(), elem)


    def test_get_cell_out_of_bounds(self):
        w,h = 2, 2
        p1 = Point(w + 1, h + 1)
        p2 = Point(-w , -h )

        _, field = create_field(w,h)

        field.get_cell_content(p1)

        field.set_cell_content(p1, Element())
        self.assertEqual(field.get_set_cell_content_status(), Field.GET_CELL_ERR)
        field.set_cell_content(p2, Element())
        self.assertEqual(field.get_set_cell_content_status(), Field.GET_CELL_ERR)



class TestFieldRemoveCell(unittest.TestCase):
    def test_rem_cell_empty(self):
        w, h = 2, 2
        p = Point(w - 1, h - 1)

        _, field = create_field(w, h)
        self.assertEqual(field.get_remove_cell_content_status(), Field.REM_CELL_NIL)

        field.remove_cell_content(p)

        self.assertEqual(field.get_remove_cell_content_status(), Field.REM_CELL_ERR)


    def test_rem_cell_out_of_bounds(self):
        w, h = 2, 2
        p = Point(w + 1, h + 1)

        _, field = create_field(w,h)
        self.assertEqual(field.get_remove_cell_content_status(), Field.REM_CELL_NIL)

        field.remove_cell_content(p)

        self.assertEqual(field.get_remove_cell_content_status(), Field.REM_CELL_ERR)


    def test_rem_cell(self):
        w, h = 2, 2
        p = Point(w - 1, h - 1)

        _, field = create_field(w,h)
        self.assertEqual(field.get_remove_cell_content_status(), Field.REM_CELL_NIL)

        field.set_cell_content(p, Element())
        field.remove_cell_content(p)

        self.assertEqual(field.get_remove_cell_content_status(), Field.REM_CELL_OK)
        
        field.query_cell(p)
        self.assertEqual(field.get_query_cell_status(), Field.QRY_CELL_OK)
        self.assertTrue(field.is_cell_empty())
