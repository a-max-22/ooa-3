from State import State

class Subscriber:
    def __init__(self):
        pass

    def on_event(self, state:State):
        pass


class Dispatcher:
    REG_NIL = 0
    REG_OK  = 1
    REG_ERR = 2

    def __init__(self):
        self.is_running_flag = False
        self.state_change_subscribers = []
        self.register_subscriber_status = self.REG_NIL
        self.state = State()

    def _notify_subscribers(self):
        for s in self.state_change_subscribers:
            s.on_event(self.state)

    def register_subscriber(self, subscriber:Subscriber):
        if not isinstance(subscriber, Subscriber):
            self.register_subscriber_status = self.REG_ERR
            return
        
        self.state_change_subscribers.append(subscriber)
        self.register_subscriber_status = self.REG_OK


    def run(self):
        self.is_running_flag = True
    
    def stop(self):
        self.is_running_flag = False

    def is_running(self):
        return self.is_running_flag


    def get_register_subscriber_status(self):
        return self.register_subscriber_status