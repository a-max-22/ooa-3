from Element import Element, VoidElem

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y 


class Dimensions:
    def __init__(self, width:int, height:int):
        assert width > 0 and height > 0, "wrong dimensions parameters"
        self.width = width
        self.height = height

    def is_point_in_dimensions(self, point:Point):
        return 0 <= point.x < self.width and 0 <= point.y < self.height


def point_advance_downtop(dim:Dimensions, point:Point):
    if point.x == dim.width - 1:
        point.x = 0
        point.y += 1
    else:
        point.x += 1

    return point

def point_advance_topdown(dims, point) -> Point:
    if point.x == 0:
        point.x = dims.width - 1
        point.y -= 1
    else:
        point.x -= 1
    return point




class Box:
    SET_CELL_NIL = 0
    SET_CELL_OK = 1
    SET_CELL_ERR = 2

    def __init__(self, dim:Dimensions, default_cell_val = None):
        self.dimensions = dim
        self.cells = [[default_cell_val for _ in range(dim.width)] \
                      for _ in range(dim.height)]
        self.set_cell_status = self.SET_CELL_NIL

    def get_cell(self, point:Point) -> Element:
        if not self.dimensions.is_point_in_dimensions(point):
            return VoidElem
        
        return self.cells[point.y][point.x]

    
    def set_cell(self, point:Point, elem:Element):
        if not self.dimensions.is_point_in_dimensions(point):
            self.set_cell_status = self.SET_CELL_ERR
            return
        
        self.set_cell_status = self.SET_CELL_OK
        self.cells[point.y][point.x] = elem


    def get_set_cell_status(self):
        return self.set_cell_status