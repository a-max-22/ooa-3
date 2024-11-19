
from State import State, Key, retreive_element, save_elem_to_state
from Field import Field
from Movements import move_elements_down, swap_cells, MOVE_OK
from DestroyElements import destroy_similar_elements
from GenerateElements import generate_first_row_elems
from UserInput import UserInput, get_point

def rule_move_elems_down(field_key: Key, state: State) -> tuple[State, bool]:
    field = retreive_element(field_key, state)

    move_status, field = move_elements_down(field)
    was_state_changed = (move_status == MOVE_OK)

    return save_elem_to_state(field_key, field, state), was_state_changed


def rule_destroy_elems(property_name:str, field_key: Key, state: State) -> tuple[State, bool]:
    field = retreive_element(field_key, state)

    field, was_state_changed = destroy_similar_elements(field, property_name)
    
    return save_elem_to_state(field_key, field, state), was_state_changed


def rule_generate_elems(property_name:str, field_key: Key, state: State) -> tuple[State, bool]:
    field = retreive_element(field_key, state)

    field, was_state_changed = generate_first_row_elems(field, property_name)
    
    return save_elem_to_state(field_key, field, state), was_state_changed


def rule_user_action(user_input:UserInput, field_key: Key, state: State) -> tuple[State, bool]:
    src, read_ok = get_point(user_input)
    was_state_changed = False
    if not read_ok:
        return state, was_state_changed  

    dst, read_ok = get_point(user_input)
    if not read_ok:
        return state, was_state_changed  
    
    if src == dst:
        return state, was_state_changed  

    field = retreive_element(field_key, state)
    status, field = swap_cells(field, src, dst)
    if status != MOVE_OK:
        print("rule_user_action, swap_cells:(%d,%d)-(%d,%d)", src.x, src.y, dst.x, dst.y)
        return state, was_state_changed  
    
    was_state_changed = True
    return state, was_state_changed