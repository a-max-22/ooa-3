from Box import Point

class UserInput:
    READ_NIL = 0
    READ_OK  = 1
    READ_ERR = 2

    def __init__(self) -> None:
        self.read_input_status = self.READ_NIL
        self.last_input_data = None 

    def get(self):
        pass

    def get_input_data(self):
        return self.last_input_data
    
    def get_read_input_status(self):
        return self.read_input_status


class ConsoleInput(UserInput):
    def __init__(self, prompt:str) -> None:
        super().__init__()
        self.prompt = prompt

    def get(self):
        self.last_input_data = input(self.prompt)
        self.read_input_status = self.READ_OK


def get_point(user_input:UserInput) -> tuple[Point, bool]:
    was_point_read_successfully = False
    user_input.get()
    if user_input.get_read_input_status() != user_input.READ_OK:
        return None, was_point_read_successfully 
    
    in_str = user_input.get_input_data()
    try:
        in_str.strip()
        x_str, y_str = in_str.split(" ", 1)
        p = Point(int(x_str), int(y_str))
        was_point_read_successfully = True
    except ValueError:
        p = None
        was_point_read_successfully = False
    
    return p, was_point_read_successfully 

