import unittest
from Element import kind_property_name
from Utils import generate_field, is_field_corresponds_to_layout
from GenerateElements import generate_first_row_elems

class TestGenerate(unittest.TestCase):
    def test_gen_elements(self):
        layout = [ [1, 0, 0],
                   [0, 0, 1] ]

        result_layout =\
                 [ [1, 1, 1],
                   [0, 0, 1] ]

        field = generate_field(layout)
        
        field, was_changed = generate_first_row_elems(field, kind_property_name)
        self.assertTrue(was_changed)
        self.assertTrue(is_field_corresponds_to_layout(field, result_layout))


    def test_gen_elements_1(self):
        layout = [ [1, 0, 0] ]

        result_layout = [ [1, 1, 1] ]

        field = generate_field(layout)
        
        field, was_changed = generate_first_row_elems(field, kind_property_name)
        
        self.assertTrue(was_changed)
        self.assertTrue(is_field_corresponds_to_layout(field, result_layout))


    def test_gen_elements_2(self):
        layout = [ [0, 0, 0],
                   [0, 0, 1], 
                   [0, 0, 0],]

        result_layout =\
                 [ [1, 1, 1],
                   [0, 0, 1],
                   [0, 0, 0], ]

        field = generate_field(layout)
        
        field, was_changed = generate_first_row_elems(field, kind_property_name)
        
        self.assertTrue(was_changed)
        self.assertTrue(is_field_corresponds_to_layout(field, result_layout))
