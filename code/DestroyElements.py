
from Field import Field
from Box import Point,  point_advance_downtop
from Element import VoidElem, kind_property_name


def advance_point(point:Point, delta):
    dx, dy = delta
    return Point(point.x + dx, point.y + dy)

def get_elem_property(field:Field, point:Point, property_name:str):
    field.get_cell_content(point)
    if field.get_get_cell_content_status() != field.GET_CELL_OK:
        return VoidElem
    
    elem = field.get_get_cell_content_result()
    
    elem.get_property(property_name)
    if elem.get_get_property_status() != elem.GET_PROP_OK:
        return VoidElem
    
    prop = elem.get_get_property_result()
    return prop


def print_field_props(field:Field):
    dims = field.get_dimensions()
    for y in range(0, dims.height):
        print('')
        for x in range(0, dims.width):
            p = Point(x,y)
            prop = get_elem_property(field, p, property_name = kind_property_name)
            print(prop, ',', end = '')
        

def collect_points_in_a_row(field:Field, start:Point, delta, property_name:str) -> list[Point]:
    points_in_row = [start]
    
    prop_to_compare = get_elem_property(field, start, property_name)
    if prop_to_compare == VoidElem: 
        return points_in_row
    
    current_point = start
    next_point = current_point
    dims = field.get_dimensions()

    while dims.is_point_in_dimensions(current_point):
        current_point = next_point
        next_point = advance_point(current_point, delta)
                    
        prop = get_elem_property(field, next_point, property_name)
        if prop_to_compare == VoidElem:
            break
        if prop_to_compare != prop:
            break
        points_in_row.append(next_point)

    return points_in_row


def collect_points_with_same_props(field: Field, start:Point, property_name:str) -> list[Point]:
    deltas = [(1,0), (1,1), (0,1), (-1,1)]
    points = []
    max_len = 0
    for delta in deltas:
        cur_points = collect_points_in_a_row(field, start, delta, property_name)
        has_three_in_a_row = (len(cur_points) >= 3)
        if not has_three_in_a_row:
            continue
        if len(cur_points) > max_len:
            points = cur_points
    return points


def destroy_similar_elements_from_start_point(field: Field, start:Point, property_name:str) -> tuple[Field, bool]:
    points = collect_points_with_same_props(field, start, property_name)
    has_three_in_a_row = (len(points) >= 3)
    were_elements_destroyed = has_three_in_a_row
    
    if not has_three_in_a_row:
        return field, were_elements_destroyed
    
    for point in points:
        field.remove_cell_content(point)

    return field, were_elements_destroyed


def destroy_similar_elements(field: Field, property_name:str) -> tuple[Field, bool]:
    dim = field.get_dimensions()

    start = Point(0, 0)
    end = Point(dim.width - 1, dim.height - 1)
    curr_point = start

    while curr_point != end:
        field, were_elems_destroyed = destroy_similar_elements_from_start_point(field, start, property_name)
        if were_elems_destroyed:
            return field, were_elems_destroyed

        curr_point = point_advance_downtop(dim, curr_point)
    
    return field, were_elems_destroyed