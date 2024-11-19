import random

from Field import Field
from Box import Point, Dimensions, point_advance_downtop 
from Element import Element, VoidElem, ElementKinds, kind_property_name


def gen_elem(field:Field, point:Point, prop_name):
    possible_values = list([e for e in ElementKinds if e!=ElementKinds.EMPTY])
    new_prop = random.choice(possible_values)
    props = {kind_property_name:new_prop}
    return  Element(props)
 

def generate_first_row_elems(field:Field, prop_name:str) -> tuple[Field,bool]:
    dim = field.get_dimensions()
    was_field_changed = False 

    start = Point(0, 0)
    end = Point(0, 1)

    current_point = start

    while current_point != end:
        field.query_cell(current_point)
        if field.get_query_cell_status() != field.QRY_CELL_OK:
            break

        if not field.is_cell_empty():
            current_point = point_advance_downtop(dim, current_point)
            continue

        was_field_changed = True
        elem = gen_elem(field, current_point, prop_name)
        field.set_cell_content(current_point, elem)
        assert field.get_set_cell_content_status() == field.SET_CELL_OK
        current_point = point_advance_downtop(dim, current_point)

    return field, was_field_changed