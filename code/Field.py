from Element import Element,VoidElem
from Box import Dimensions, Box, Point


class Field(Element):
    CREATE_OK = 1
    CREATE_ERR = 2

    CELL_EMPTY = 0
    CELL_OCCUPIED = 1

    GET_CELL_NIL = 0
    GET_CELL_OK = 1
    GET_CELL_ERR = 2

    REM_CELL_NIL = 0
    REM_CELL_OK = 1
    REM_CELL_ERR = 2

    SET_CELL_NIL = 0
    SET_CELL_OK = 1
    SET_CELL_ERR = 2

    QRY_CELL_NIL = 0
    QRY_CELL_OK = 1
    QRY_CELL_ERR = 2

    def __init__(self, dimensions:Dimensions):
        self.dimensions = dimensions
        self.last_queried_cell_content = None
        self.get_cell_content_status =  self.GET_CELL_NIL
        self.rem_cell_content_status =  self.REM_CELL_NIL
        self.set_cell_content_status =  self.SET_CELL_NIL
        self.query_cell_status = self.QRY_CELL_NIL

        self.is_last_queried_cell_empty = False
        
        self.empty_cell_value = None

        self.box = Box(dimensions, default_cell_val = self.empty_cell_value) 


    def _is_cell_empty_internal(self, point:Point):
        cell = self.box.get_cell(point)
        return cell is self.empty_cell_value

    def _set_cell_empty_internal(self, point:Point):
        self.box.set_cell(point, self.empty_cell_value)
    
    # предусловие: координаты находятся в пределах поля;
    # постусловие: в статус  последней запрошенной клетки помещены сведени о том, пустая она или нет
    def query_cell(self, point:Point):
        cell = self.box.get_cell(point)
        if cell == VoidElem:
            self.query_cell_status = self.QRY_CELL_ERR
            return

        self.is_last_queried_cell_empty = self._is_cell_empty_internal(point)
        self.query_cell_status = self.QRY_CELL_OK


    # предусловие: координаты находятся в пределах поля; клетка непустая
    # постусловие: в статус  последней запрошенной клетки помещены сведени о том, пустая она или нет
    def get_cell_content(self, point:Point):
        cell = self.box.get_cell(point)
        if cell == VoidElem:
            self.get_cell_content_status = self.GET_CELL_ERR
            return 
        
        if self._is_cell_empty_internal(point):
            self.get_cell_content_status = self.GET_CELL_ERR
            return 

        self.get_cell_content_status = self.GET_CELL_OK
        self.last_queried_cell_content = cell


    # предусловие: координаты находятся в пределах поля; клетка с заданным координатами непуста
    # постусловие: из клетки с заданными координатами удалено содержимое
    def remove_cell_content(self, point:Point):
        cell = self.box.get_cell(point)
        if cell == VoidElem:
            self.rem_cell_content_status = self.REM_CELL_ERR
            return 

        if self._is_cell_empty_internal(point):
            self.rem_cell_content_status = self.REM_CELL_ERR
            return 
        
        self._set_cell_empty_internal(point)
        self.rem_cell_content_status = self.REM_CELL_OK
        

    # предусловие: координаты находятся в пределах поля; клетка с заданным координатами пуста
    # постусловие: в клетку с заданными координатами помещен элемент
    def set_cell_content(self, point:Point, elem:Element):
        cell = self.box.get_cell(point)
        if cell == VoidElem:
            self.set_cell_content_status = self.SET_CELL_ERR
            return

        if not self._is_cell_empty_internal(point):
            self.set_cell_content_status = self.SET_CELL_ERR
            return 
        
        self.box.set_cell(point, elem)
        self.set_cell_content_status = self.SET_CELL_OK
    

    def get_get_cell_content_result(self) -> Element|None:
        return self.last_queried_cell_content

    def get_get_cell_content_status(self):
        return self.get_cell_content_status

    def get_set_cell_content_status(self):
        return self.set_cell_content_status

    def get_remove_cell_content_status(self):
        return self.rem_cell_content_status

    def get_query_cell_status(self):
        return self.query_cell_status
    
    def is_cell_empty(self) -> bool:
        return self.is_last_queried_cell_empty

    def get_dimensions(self) -> Dimensions:
        return self.dimensions

def create_field(width, height) -> tuple[int,Field]:
    if width > 0 and height > 0:
        return Field.CREATE_OK, Field(Dimensions(width, height))
    
    return Field.CREATE_ERR, None