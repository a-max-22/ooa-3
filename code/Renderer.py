from Dispatcher import Subscriber
from State import State, Key


class Renderer(Subscriber):
    def __init__(self):
        super().__init__()

    def update_layout(self, state:State):
        pass

    def draw(self):
        pass

    def clear(self):
        pass

    def on_event(self, state: State):
        self.update_layout(state)
        self.clear()
        self.draw()
        super().on_event(state)


