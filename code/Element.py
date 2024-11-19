from enum import Enum

class Element:
    GET_PROP_NIL = 0
    GET_PROP_OK = 1
    GET_PROP_ERR = 2

    def __init__(self, properties = None):
        if properties is None: 
            self.properties = {}
        else:
            self.properties = properties
        self.get_property_status = self.GET_PROP_NIL
        self.last_queried_property = None 
    
    def get_property(self, prop_name:str):
        if prop_name not in self.properties:
            self.get_property_status = self.GET_PROP_ERR
            return 
        
        self.get_property_status = self.GET_PROP_OK
        self.last_queried_property = self.properties[prop_name]

    def get_get_property_status(self):
        return self.get_property_status
    
    def get_get_property_result(self):
        return self.last_queried_property
    
class Property:
    pass

class VoidElement(Element,Property):
    def get_property(self, prop_name:str):
        raise AttributeError("can't get property of void element object")
    
    def get_get_property_status(self):
        raise AttributeError("can't get get_property_status of void element object")
    
    def get_get_property_result(self):
        raise AttributeError("can't get get_property_result  of void element object")


VoidElem = VoidElement()

class ElementKinds(Enum):
    EMPTY = 0
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6

kind_property_name = "kind"
