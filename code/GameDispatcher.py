from Dispatcher import Dispatcher
from Field import create_field
from Rules import rule_generate_elems, rule_move_elems_down, rule_destroy_elems, rule_user_action
from Element import kind_property_name
from SimpleConsoleRenderer import SimpleConsoleFieldRenderer
from UserInput import ConsoleInput


class GameDispatcher(Dispatcher):
    def __init__(self):
        super().__init__()
        
        _, field = create_field(4, 4)
        state = self.state
        state.save_element(field)
        assert state.get_save_element_status() == state.SAVE_OK
        self.field_key = self.state.get_saved_element_key()

        self.rule_gen_elements = lambda field_key, state: \
            rule_generate_elems(kind_property_name, field_key, state) 
        
        prompt = "Enter point coordinate in format 'x y': "
        self.rule_user_input = lambda field_key, state: \
            rule_user_action(ConsoleInput(prompt), field_key, state) 
        
        self.rule_destroy_elems = lambda field_key, state: \
            rule_destroy_elems(kind_property_name, field_key, state) 
        
        field_renderer = SimpleConsoleFieldRenderer(self.field_key)
        self.register_subscriber(field_renderer)


    def _apply_single_rule_until_no_changes(self, rule) -> bool:
        was_state_changed = True
        was_change = False
        while was_state_changed:
            state, was_state_changed = rule(self.field_key, self.state)
            if was_state_changed:
                self._notify_subscribers()
                was_change = True
            self.state = state
        return was_change
            

    def _apply_each_rule_until_no_changes(self, rules):
        in_progress = True

        while in_progress:
            in_progress = False
            for rule in rules:
                was_change = self._apply_single_rule_until_no_changes(rule)
                if was_change:
                    in_progress = True
                    break

    def _apply_rules_once(self, rules):
        was_change = False
        for rule in rules:
            state, was_state_changed = rule(self.field_key, self.state)
            if was_state_changed:
                self._notify_subscribers()
                was_change = True
            self.state = state
        return was_change

    def _apply_rule_sequence_until_no_changes(self, rules):
        in_progress = True

        while in_progress:
            in_progress = False
            was_change = self._apply_rules_once(rules)
            if was_change:
                in_progress = True

   
    def run(self):
        game_finished = False
        while not game_finished:
            generate_field_rules = [self.rule_gen_elements, rule_move_elems_down]
            self._apply_each_rule_until_no_changes(generate_field_rules)
    
            c = input("press 'q' if you want to exit, any other key if you want to continue ")
            if c == 'q':
                game_finished = True
                break
            
            self._apply_rules_once([self.rule_user_input])
            self._apply_rule_sequence_until_no_changes([self.rule_destroy_elems,\
                                                        rule_move_elems_down])
