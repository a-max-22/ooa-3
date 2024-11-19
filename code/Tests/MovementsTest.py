import unittest
from  Field import Point
from Movements import move_to_empty_cell, move_elements_down, MOVE_OK, MOVE_ERR, MOVE_NIL, swap_cells
from Utils import generate_field, is_field_corresponds_to_layout


class TestMoveToEmptyCell(unittest.TestCase):
    def test_valid_move(self):
        layout = [ [1, 0],
                   [0, 0] ]
        
        field = generate_field(layout)

        src = Point(0, 0)
        dst = Point(0, 1)
        
        field.get_cell_content(src)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        src_elem = field.get_get_cell_content_result()

        status, field = move_to_empty_cell(field, src, dst)
        self.assertEqual(status, MOVE_OK)

        field.get_cell_content(dst)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        dst_elem = field.get_get_cell_content_result()

        self.assertEqual(dst_elem, src_elem)
        
        field.query_cell(src)
        self.assertEqual(field.get_query_cell_status(), field.QRY_CELL_OK)
        self.assertTrue(field.is_cell_empty())


    
    def test_move_out_of_field(self):
        layout = [ [1, 0],
                   [0, 0] ]

        field = generate_field(layout)

        src = Point(0, 0)
        dst = Point(0, 2)
        
        field.get_cell_content(src)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        cell_before_move = field.get_get_cell_content_result()

        status, field = move_to_empty_cell(field, src, dst)
        self.assertEqual(status, MOVE_ERR)
        
        field.query_cell(src)
        self.assertEqual(field.get_query_cell_status(), field.QRY_CELL_OK)
        self.assertFalse(field.is_cell_empty())


        field.get_cell_content(src)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        cell_after_move = field.get_get_cell_content_result()
        self.assertEqual(cell_before_move, cell_after_move)
    

    def test_move_to_non_empty(self):
        layout = [ [1, 0],\
                   [0, 1] ]

        field = generate_field(layout)

        src = Point(0, 0)
        dst = Point(1, 1)
        
        field.get_cell_content(src)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        src_cell = field.get_get_cell_content_result()

        field.get_cell_content(dst)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        dst_cell = field.get_get_cell_content_result()

        status, field = move_to_empty_cell(field, src, dst)
        self.assertEqual(status, MOVE_ERR)
        
        field.query_cell(src)
        self.assertEqual(field.get_query_cell_status(), field.QRY_CELL_OK)
        self.assertFalse(field.is_cell_empty())

        field.query_cell(dst)
        self.assertEqual(field.get_query_cell_status(), field.QRY_CELL_OK)
        self.assertFalse(field.is_cell_empty())

        field.get_cell_content(src)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        src_cell_after = field.get_get_cell_content_result()

        field.get_cell_content(dst)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        dst_cell_after = field.get_get_cell_content_result()

        self.assertEqual(src_cell, src_cell_after)
        self.assertEqual(dst_cell, dst_cell_after)


    def test_valid_move_2(self):
        layout = [ [1, 0],
                   [0, 0] ]
        
        layout_after_move = \
                 [ [0, 0],
                   [1, 0] ]

        field = generate_field(layout)

        src = Point(0, 0)
        dst = Point(0, 1)
        
        field.get_cell_content(src)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        src_elem = field.get_get_cell_content_result()

        status, field = move_to_empty_cell(field, src, dst)
        self.assertEqual(status, MOVE_OK)

        field.get_cell_content(dst)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        dst_elem = field.get_get_cell_content_result()

        self.assertEqual(dst_elem, src_elem)
        
        field.query_cell(src)
        self.assertEqual(field.get_query_cell_status(), field.QRY_CELL_OK)
        self.assertTrue(field.is_cell_empty())

        self.assertTrue(is_field_corresponds_to_layout(field, layout_after_move))



class TestSwapCells(unittest.TestCase):
    def test_valid_swap(self):
        layout = [ [1, 0],\
                   [0, 1] ]

        field = generate_field(layout)

        src = Point(0, 0)
        dst = Point(1, 1)
        
        field.get_cell_content(src)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        src_cell = field.get_get_cell_content_result()

        field.get_cell_content(dst)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        dst_cell = field.get_get_cell_content_result()

        status, field = swap_cells(field, src, dst)
        self.assertEqual(status, MOVE_OK)
        
        field.query_cell(src)
        self.assertEqual(field.get_query_cell_status(), field.QRY_CELL_OK)
        self.assertFalse(field.is_cell_empty())

        field.query_cell(dst)
        self.assertEqual(field.get_query_cell_status(), field.QRY_CELL_OK)
        self.assertFalse(field.is_cell_empty())

        field.get_cell_content(src)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        src_cell_after = field.get_get_cell_content_result()

        field.get_cell_content(dst)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        dst_cell_after = field.get_get_cell_content_result()

        self.assertEqual(src_cell, dst_cell_after)
        self.assertEqual(dst_cell, src_cell_after)


    def test_swap_with_empty(self):
        layout = [ [1, 0],\
                   [0, 0] ]

        field = generate_field(layout)

        src = Point(0, 0)
        dst = Point(0, 1)

        field.get_cell_content(src)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        src_cell = field.get_get_cell_content_result()

        status, field = swap_cells(field, src, dst)
        self.assertEqual(status, MOVE_ERR)
        
        field.query_cell(src)
        self.assertEqual(field.get_query_cell_status(), field.QRY_CELL_OK)
        self.assertFalse(field.is_cell_empty())

        field.query_cell(dst)
        self.assertEqual(field.get_query_cell_status(), field.QRY_CELL_OK)
        self.assertTrue(field.is_cell_empty())

        field.get_cell_content(src)

        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        src_cell_after = field.get_get_cell_content_result()

        field.query_cell(dst)
        self.assertEqual(field.get_query_cell_status(), field.QRY_CELL_OK)
        self.assertTrue(field.is_cell_empty())

        self.assertEqual(src_cell, src_cell_after)



    def test_swap_with_out_of_bounds(self):
        layout = [ [1, 0],\
                   [0, 0] ]

        field = generate_field(layout)

        src = Point(0, 0)
        dst = Point(-1, -1)

        field.get_cell_content(src)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        src_cell = field.get_get_cell_content_result()

        status, field = swap_cells(field, src, dst)
        self.assertEqual(status, MOVE_ERR)
        
        field.query_cell(src)
        self.assertEqual(field.get_query_cell_status(), field.QRY_CELL_OK)
        self.assertFalse(field.is_cell_empty())

        field.get_cell_content(src)

        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        src_cell_after = field.get_get_cell_content_result()

        self.assertEqual(src_cell, src_cell_after)


class TestMoveToEmptyCell(unittest.TestCase):
    def test_movement(self):
        layout = [ [1, 0],
                   [0, 0] ]
        
        layout_after_move = \
                 [ [0, 0],
                   [1, 0] ]

        field = generate_field(layout)

        src = Point(0, 0)
        dst = Point(0, 1)
        
        field.get_cell_content(src)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        src_elem = field.get_get_cell_content_result()

        status, field = move_elements_down(field)
        self.assertEqual(status, MOVE_OK)

        field.get_cell_content(dst)
        self.assertEqual(field.get_get_cell_content_status(), field.GET_CELL_OK)
        dst_elem = field.get_get_cell_content_result()

        self.assertEqual(dst_elem, src_elem)
        
        field.query_cell(src)
        self.assertEqual(field.get_query_cell_status(), field.QRY_CELL_OK)
        self.assertTrue(field.is_cell_empty())

        self.assertTrue(is_field_corresponds_to_layout(field, layout_after_move))


    def test_movement_2(self):
        layout = [ [1, 0, 1],
                   [0, 1, 0] ]
        
        layout_after_move = \
                 [ [0, 0, 0],
                   [1, 1, 1] ]

        field = generate_field(layout)
        

        status, field = move_elements_down(field)
        self.assertEqual(status, MOVE_OK)

        self.assertTrue(is_field_corresponds_to_layout(field, layout_after_move))\


    def test_movement_3(self):
        layout = [ [1, 0, 1],
                   [1, 0, 1],
                   [0, 1, 0] ]
        
        layout_after_move = \
                 [ [0, 0, 0],
                   [1, 0, 1],
                   [1, 1, 1] ]

        field = generate_field(layout)
        
        status, field = move_elements_down(field)
        self.assertEqual(status, MOVE_OK)

        self.assertTrue(is_field_corresponds_to_layout(field, layout_after_move))


    def test_no_movement_1(self):
        layout = [ [1, 0, 1] ]
        
        layout_after_move = \
                 [ [1, 0, 1] ]

        field = generate_field(layout)
        

        status, field = move_elements_down(field)
        self.assertEqual(status, MOVE_NIL)

        
        self.assertTrue(is_field_corresponds_to_layout(field, layout_after_move))


    def test_no_movement_2(self):
        layout = [ [0, 0, 0], 
                   [0, 1, 1]]
        
        layout_after_move = layout

        field = generate_field(layout)
        

        status, field = move_elements_down(field)
        self.assertEqual(status, MOVE_NIL)
        
        self.assertTrue(is_field_corresponds_to_layout(field, layout_after_move))
