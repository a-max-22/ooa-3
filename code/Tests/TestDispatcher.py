import unittest
from  Dispatcher import Dispatcher

class TestDispatcher(unittest.TestCase):
    def test_is_running_on_creation(self):
        d = Dispatcher()
        self.assertFalse(d.is_running())

    def test_is_running_on_launch(self):
        d = Dispatcher()
        d.run()
        self.assertTrue(d.is_running())
    
    def test_is_running_on_stop(self):
        d = Dispatcher()
        d.run()
        d.stop()
        self.assertFalse(d.is_running())
