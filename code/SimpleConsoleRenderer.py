from Renderer import Renderer
from Field import Field
from State import State, Key, retreive_element
from Element import ElementKinds, kind_property_name
from Utils import layout_validate_and_get_dimensions, generate_field_with_kinds
from Box import Point

kinds_to_letters = {
    ElementKinds.A:'A',
    ElementKinds.B:'B',
    ElementKinds.C:'C',
    ElementKinds.D:'D',
    ElementKinds.E:'E',
    ElementKinds.F:'F',

    ElementKinds.EMPTY:' '
}


class Layout(list[list[int]]):
    pass

def make_field_layout(field:Field, props_to_names:dict,
                      empty_key = ElementKinds.EMPTY) -> Layout:
    dim =  field.get_dimensions()
    layout = Layout([[None for _ in range(dim.width)] \
                    for _ in range(dim.height)])

    for y in range(0, dim.height):
        for x in range(0, dim.width):
            p = Point(x,y)

            field.query_cell(p)
            assert field.get_query_cell_status() == field.QRY_CELL_OK

            if field.is_cell_empty():
                layout[y][x] = props_to_names[empty_key]
                continue 
            

            field.get_cell_content(p)
            assert field.get_get_cell_content_status() == field.GET_CELL_OK

            elem = field.get_get_cell_content_result()
            
            elem.get_property(kind_property_name)
            assert elem.get_get_property_status() == elem.GET_PROP_OK

            prop = elem.get_get_property_result()
            layout[y][x] = props_to_names[prop]
    
    return layout



def print_layout(layout:Layout):
    width, height = layout_validate_and_get_dimensions(layout)
    
    print(' '*4, end='')
    for i in range(0, width):
        print('  %d ' %i, end ='')

    for y in range(0, height):
        for x in range(0, width):
            if x == 0:
                print('')
                print("%d: " % y, end ='')
                print(' | ', end ='')
            print(layout[y][x], end ='')
            print(' | ', end ='')



class SimpleConsoleFieldRenderer(Renderer):
    def __init__(self, field_key:Key):
        self.field_key = field_key
        self.layout = Layout()
    
    def update_layout(self, state:State):
        field = retreive_element(self.field_key, state)
        self.layout = make_field_layout(field, kinds_to_letters)
        
    def draw(self):
        print('')
        print('_'*20)
        print_layout(self.layout)
        print('')


def test_print_layout():
        A = ElementKinds.A
        B = ElementKinds.B
        C = ElementKinds.C
        D = ElementKinds.D

        initial_layout = \
                 [ [B, D, C, A],
                   [C, A, C, B],
                   [D, B, A, B], 
                   [C, C, C, A], ]
        
        field = generate_field_with_kinds(initial_layout)

        result_layout = make_field_layout(field, kinds_to_letters)
        print_layout(result_layout)
