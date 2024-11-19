from Field import Field 
from Box import Point, Dimensions, point_advance_topdown
from Element import Element

MOVE_NIL = 0    
MOVE_OK  = 1
MOVE_ERR = 2

def move_to_empty_cell(field: Field, src:Point, dst:Point) -> tuple[int, Field]:
    field.query_cell(dst)
    if field.get_query_cell_status() != field.QRY_CELL_OK:
        return MOVE_ERR, field
    
    if not field.is_cell_empty():
        return MOVE_ERR, field

    field.get_cell_content(src)
    if field.get_get_cell_content_status() != Field.GET_CELL_OK:
        return MOVE_ERR, field
    
    moved_elem = field.get_get_cell_content_result()
    
    field.remove_cell_content(src)
    if field.get_remove_cell_content_status() != field.REM_CELL_OK:
        return MOVE_ERR, field

    field.set_cell_content(dst, moved_elem)
    if field.get_set_cell_content_status() != field.SET_CELL_OK:
        return MOVE_ERR, field

    return MOVE_OK, field



def swap_cells(field: Field, src:Point, dst:Point) -> tuple[int, Field]:
    field.get_cell_content(dst)
    if field.get_get_cell_content_status() != Field.GET_CELL_OK:
        return MOVE_ERR, field
    
    dst_elem = field.get_get_cell_content_result()

    field.remove_cell_content(dst)
    if field.get_remove_cell_content_status() != Field.REM_CELL_OK:
        return MOVE_ERR, field

    status, field = move_to_empty_cell(field, src, dst)
    if status != MOVE_OK:
        return MOVE_ERR, field
    
    field.set_cell_content(src, dst_elem)
    if field.get_set_cell_content_status() != Field.SET_CELL_OK:
        return MOVE_ERR, field

    return MOVE_OK, field


def move_elements_down(field: Field) -> tuple[int, Field]:
    dims = field.get_dimensions()
    initial_point = Point(dims.width - 1, dims.height - 1)
    stop_point = Point(1, 0)
    current_point = initial_point

    move_status = MOVE_NIL

    while current_point != stop_point:
        field.query_cell(current_point)
        if field.get_query_cell_status() != field.QRY_CELL_OK:
            return MOVE_ERR, field
        
        if not field.is_cell_empty():
            current_point = point_advance_topdown(dims, current_point)
            continue
        
        upper_point = Point(current_point.x, current_point.y - 1)
        status, field = move_to_empty_cell(field, upper_point, current_point)
        if status == MOVE_OK:
            move_status = MOVE_OK

        current_point = point_advance_topdown(dims, current_point)


    return move_status, field