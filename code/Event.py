from typing import Callable
from State import State

class Event:
    APPLY_NIL = 0
    APPLY_OK  = 1
    APPLY_ERR = 2

    def __init__(self, rule:Callable[[State], State]):
        self.rule = rule
        self.is_event_applied = False
        self.apply_status = self.APPLY_NIL

    def apply(self, state:State) -> State:
        if self.is_event_applied:
            self.apply_status = self.APPLY_ERR
            return state
        
        new_state = self.rule(state)
        self.is_event_applied = True
        self.apply_status = self.APPLY_OK
        return new_state
    
    def get_apply_status(self):
        return self.apply_status