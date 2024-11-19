import unittest
from  State import State, Key, Element


class TestState(unittest.TestCase):
    def test_status_on_creation(self):
        s = State()
        self.assertEqual(s.get_get_element_status(), s.GET_ELEM_NIL)
        self.assertEqual(s.get_save_element_status(), s.SAVE_NIL)
        self.assertEqual(s.get_remove_element_status(), s.REM_NIL)
        self.assertEqual(s.get_update_element_status(), s.UPD_ELEM_NIL)

    def test_status_on_save(self):
        s = State()
        elem = Element()
        s.save_element(elem)
        self.assertEqual(s.get_save_element_status(), s.SAVE_OK)
        self.assertIsInstance(s.get_saved_element_key(), Key)

    def test_double_save_same_element(self):
        s = State()
        elem = Element()
        s.save_element(elem)
        s.save_element(elem)

        self.assertEqual(s.get_save_element_status(), s.SAVE_ERR)

    def test_get_elem(self):
        s = State()
        elem = Element()
        s.save_element(elem)
        self.assertEqual(s.get_save_element_status(), s.SAVE_OK)

        key = s.get_saved_element_key()
        
        s.get_element(key)
        saved_elem = s.get_get_element_result()
        self.assertEqual(elem, saved_elem)
        self.assertEqual(s.get_get_element_status(), s.GET_ELEM_OK)

    def test_get_nonexistent_elem(self):
        s = State()
        key = Key(1)
        
        s.get_element(key)
        self.assertEqual(s.get_get_element_status(), s.GET_ELEM_ERR)


    def test_update(self):
        s = State()
        elem_old = Element()
        elem_new = Element()

        s.save_element(elem_old)
        self.assertEqual(s.get_save_element_status(), s.SAVE_OK)
        key = s.get_saved_element_key()

        s.update_element(key, elem_new)
        self.assertEqual(s.get_update_element_status(), s.UPD_ELEM_OK)

        s.get_element(key)
        saved_elem = s.get_get_element_result()
        self.assertEqual(saved_elem, elem_new)


    def test_update_non_existant(self):
        s = State()
        elem_new = Element()
        key = Key(1)

        s.update_element(key, elem_new)
        self.assertEqual(s.get_update_element_status(), s.UPD_ELEM_ERR)
