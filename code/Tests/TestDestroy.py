import unittest

from Field import Point
from Utils import generate_field_with_kinds, compare_layouts_with_kinds
from DestroyElements import destroy_similar_elements
from Element import kind_property_name

class TestDestroy(unittest.TestCase):  
    
    def test_destroy(self):
        A = 1
        B = 2
        C = 3

        initial_layout = \
                 [ [A, A, C],
                   [A, A, B],
                   [C, B, A],  ]

        result_layout = \
                 [ [0, A, C],
                   [A, 0, B],
                   [C, B, 0],  ]

        field = generate_field_with_kinds(initial_layout)
        
        field, were_elems_destroyed = destroy_similar_elements(field, kind_property_name)
        self.assertTrue(were_elems_destroyed)
        self.assertTrue(compare_layouts_with_kinds(field, result_layout))

    def test_destroy_several_rows(self):
        A = 1
        B = 2

        initial_layout = \
                 [ [A, A, A],
                   [A, A, B],
                   [A, B, A],  ]

        result_layout = \
                 [ [0, A, A],
                   [0, A, B],
                   [0, B, A],  ]

        field = generate_field_with_kinds(initial_layout)
        
        field, were_elems_destroyed = destroy_similar_elements(field, kind_property_name)
        self.assertTrue(were_elems_destroyed)
        self.assertTrue(compare_layouts_with_kinds(field, result_layout))


    def test_no_three_in_a_row(self):
        A = 1
        B = 2
        C = 3

        initial_layout = \
                 [ [A, C, C],
                   [A, A, B],
                   [C, A, C], ]

        field = generate_field_with_kinds(initial_layout)
        
        field, were_elems_destroyed = destroy_similar_elements(field, kind_property_name)

        self.assertFalse(were_elems_destroyed)
        self.assertTrue(compare_layouts_with_kinds(field, initial_layout))
    

    def test_several_threes_in_a_row(self):
        A = 1
        B = 2
        C = 3
        D = 4

        initial_layout = \
                 [ [B, D, C, A],
                   [C, A, C, B],
                   [D, B, A, B], 
                   [C, C, C, A], ]

        result_layout = \
                 [ [B, D, C, A],
                   [C, 0, C, B],
                   [D, B, 0, B], 
                   [C, C, C, 0], ]

        field = generate_field_with_kinds(initial_layout)
        
        field, were_elems_destroyed = destroy_similar_elements(field, kind_property_name)
        
        self.assertTrue(were_elems_destroyed)
        self.assertTrue(compare_layouts_with_kinds(field, result_layout))


    def test_lateral_row(self):
        A = 1
        B = 2
        C = 3
        D = 4

        initial_layout = \
                 [ [B, D, C, A],
                   [C, A, C, B],
                   [B, B, B, C], 
                   [C, A, C, A], ]

        result_layout = \
                 [ [B, D, C, A],
                   [C, A, C, B],
                   [0, 0, 0, C], 
                   [C, A, C, A], ]

        field = generate_field_with_kinds(initial_layout)
        
        field, were_elems_destroyed = destroy_similar_elements(field, kind_property_name)
        
        self.assertTrue(were_elems_destroyed)
        self.assertTrue(compare_layouts_with_kinds(field, result_layout))


    def test_diagonal_row(self):        
        A = 1
        B = 2
        C = 3
        D = 4
        
        initial_layout = \
                 [ [B, A, C, D],
                   [D, D, D, B],
                   [B, D, B, C], 
                   [C, A, C, A], ]

        result_layout = \
                 [ [B, A, C, 0],
                   [D, D, 0, B],
                   [B, 0, B, C], 
                   [C, A, C, A], ]

        field = generate_field_with_kinds(initial_layout)
        
        field, were_elems_destroyed = destroy_similar_elements(field, kind_property_name)
        
        self.assertTrue(were_elems_destroyed)
        self.assertTrue(compare_layouts_with_kinds(field, result_layout))
       
    def test_vertical_row(self):        
        A = 1
        B = 2
        C = 3
        D = 4
        
        initial_layout = \
                 [ [B, C, C, D],
                   [D, C, D, B],
                   [B, C, B, C], 
                   [A, C, C, A], ]

        result_layout = \
                 [ [B, 0, C, D],
                   [D, 0, D, B],
                   [B, 0, B, C], 
                   [A, 0, C, A], ]

        field = generate_field_with_kinds(initial_layout)
        
        field, were_elems_destroyed = destroy_similar_elements(field, kind_property_name)
        
        self.assertTrue(were_elems_destroyed)
        self.assertTrue(compare_layouts_with_kinds(field, result_layout))
       
