from Field import Field, create_field
from Box import Point
from Element import Element,  kind_property_name

def print_pts(points):
    print('print_pts:')
    for p in points:
        print("     p:", p.x, p.y)


def layout_validate_and_get_dimensions(field_layout:list[list[int]]):
    height = len(field_layout)
    assert height > 0, "generate_field: empty elements list"
    assert len(field_layout) > 0, "generate_field: height is 0"

    width = len(field_layout[0])
    assert width > 0, "generate_field: width must be more than 0"

    for row in field_layout:
        assert len(row) == width, "wrong row len, expeced %d, provided %d" % (width, len(row))

    return width, height


def generate_field(field_layout:list[list[int]]) -> Field|None:
    width, height = layout_validate_and_get_dimensions(field_layout)
    
    status, field = create_field(width, height)
    assert status == Field.CREATE_OK, "error creating field"

    for y in range(0, height):
        for x in range(0, width):
            if field_layout[y][x] == 0:
                continue
            
            p = Point(x,y)
            elem = Element()
            field.set_cell_content(p, elem)

            assert field.get_set_cell_content_status() == field.SET_CELL_OK,\
                  "error setting cell in %d, %d" %(x,y)

    return field


def is_field_corresponds_to_layout(field:Field, field_layout:list[list[int]]) -> bool:
    width, height = layout_validate_and_get_dimensions(field_layout)
    for y in range(0, height):
        for x in range(0, width):
            is_layout_cell_empty = (field_layout[y][x] == 0)
            
            p = Point(x,y)

            field.query_cell(p)
            assert field.get_query_cell_status() == field.QRY_CELL_OK

            if is_layout_cell_empty != field.is_cell_empty():
                return False

    return True



def generate_field_with_kinds(field_layout:list[list[int]]) -> Field|None:
    width, height = layout_validate_and_get_dimensions(field_layout)
    
    status, field = create_field(width, height)
    assert status == Field.CREATE_OK, "error creating field"

    for y in range(0, height):
        for x in range(0, width):
            if field_layout[y][x] == 0:
                continue
            
            p = Point(x,y)
            elem = Element({kind_property_name:field_layout[y][x]})
            field.set_cell_content(p, elem)

            assert field.get_set_cell_content_status() == field.SET_CELL_OK,\
                  "error setting cell in %d, %d" %(x,y)

    return field


def compare_layouts_with_kinds(field:Field, field_layout:list[list[int]]) -> bool:
    width, height = layout_validate_and_get_dimensions(field_layout)
    for y in range(0, height):
        for x in range(0, width):
            is_layout_cell_empty = (field_layout[y][x] == 0)
            
            p = Point(x,y)

            field.query_cell(p)
            assert field.get_query_cell_status() == field.QRY_CELL_OK

            if is_layout_cell_empty != field.is_cell_empty():
                return False
            
            if field.is_cell_empty():
                continue

            field.get_cell_content(p)
            assert field.get_get_cell_content_status() == field.GET_CELL_OK

            elem = field.get_get_cell_content_result()
            
            elem.get_property(kind_property_name)
            assert elem.get_get_property_status() == elem.GET_PROP_OK

            prop = elem.get_get_property_result()
            
            if prop != field_layout[y][x]:
                return False

    return True

