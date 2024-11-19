from Element import Element

class Key:
    def __init__(self, value) -> None:
        self.value = value
    
    def __hash__(self) -> int:
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self) -> str:
        return f'{self.value}'


def _gen_next_key():
    num = 0
    while True:
        yield Key(num)
        num += 1


class State:
    SAVE_NIL = 0
    SAVE_OK = 1
    SAVE_ERR = 2

    REM_NIL = 0
    REM_OK = 1
    REM_ERR = 2

    GET_KEY_NIL = 0
    GET_KEY_OK = 1
    GET_KEY_ERR = 2

    GET_ELEM_NIL = 0
    GET_ELEM_OK = 1
    GET_ELEM_ERR = 2

    UPD_ELEM_NIL = 0
    UPD_ELEM_OK = 1
    UPD_ELEM_ERR = 2


    def __init__(self):
        self.storage = {}
        self.elems_set = set()
        self.key_generator = _gen_next_key()
        self.get_element_status = self.GET_ELEM_NIL
        self.last_queried_elem = None
        self.save_elem_status = self.SAVE_NIL
        self.last_saved_elem_key = None
        self.remove_elem_status = self.REM_NIL
        self.update_element_status = self.UPD_ELEM_NIL

    # предусловие: элемент ранее не сохранялся в состоянии
    # постусловие: элемент сохранен в состоянии    
    def save_element(self, elem):
        if elem in self.elems_set:
            self.save_elem_status = self.SAVE_ERR
            return
        
        self.elems_set.add(elem)
        key = next(self.key_generator)
        self.storage[key] = elem
        self.save_elem_status = self.SAVE_OK
        self.last_saved_elem_key = key

    # предусловие: элемент с заданным ключом ранее был сохранен в состоянии
    # постусловие: запрошенный элемент установлен в поле в котором есть последнее состояние
    def get_element(self, key:Key):
        if not isinstance(key, Key):
            self.get_element_status = self.GET_ELEM_ERR
            return
        
        if key not in self.storage:
            self.get_element_status = self.GET_ELEM_ERR
            return

        self.get_element_status = self.GET_ELEM_OK
        self.last_queried_elem = self.storage[key]

    # предусловие: элемент c заданным ключом присутствует в состоянии
    # постусловие: элемент по заданному ключу записан новый элемент    
    def update_element(self, key:Key, elem:Element):
        if not isinstance(key, Key):
            self.update_element_status = self.UPD_ELEM_ERR
            return
        
        if key not in self.storage:
            self.update_element_status = self.UPD_ELEM_ERR
            return
        
        self.update_element_status = self.UPD_ELEM_OK
        self.storage[key] = elem


    def get_get_element_status(self):
        return self.get_element_status

    def get_get_element_result(self):
        return self.last_queried_elem

    def get_save_element_status(self):
        return self.save_elem_status

    def get_saved_element_key(self):
        return self.last_saved_elem_key

    def get_remove_element_status(self):
        return self.remove_elem_status
    
    def get_update_element_status(self):
        return self.update_element_status
    

def retreive_element(key: Key, state: State) -> Element:
    state.get_element(key)
    assert state.get_get_element_status() == state.GET_ELEM_OK, "retreive_element: no field to work with"
    
    field = state.get_get_element_result()
    assert isinstance(field, Element), "retreive_element: wrong type" 

    return field 

def save_elem_to_state(field_key: Key, elem:Element, state: State) -> State:
    state.update_element(field_key, elem)
    assert state.get_update_element_status() == state.UPD_ELEM_OK, "save_elem_to_state: update field error"
    return state

