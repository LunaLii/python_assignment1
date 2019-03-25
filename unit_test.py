from fileHandler import PrintClass
import unittest
from validator import Validator
# Happy day scenario : done
# Exceptions and edge cases : done


class TestDataExtraction(unittest.TestCase):
    # Clement
    def setUp(self):
        # be executed before each test
        self.test_class = PrintClass()

    def test_get_class_name(self):
        list_1 = ['class a {\n', '    n : String\n', '    add()\n', '}\n']
        list_2 = ['class  {\n', '    n : String\n', '    add()\n', '}\n']
        list_3 = ['    name : String\n', '    add_attributes()\n', '}\n']
        self.assertEqual(self.test_class.get_class_name(list_1), 'a')
        self.assertEqual(self.test_class.get_class_name(list_2), '')
        self.assertIsNone(self.test_class.get_class_name(list_3))

    # Luna
    def test_validate_class_name_is_true(self):
        validator = Validator()
        result_1 = validator.validate_class_name("Name")
        result_2 = validator.validate_class_name("ClassName")
        self.assertTrue(result_1)
        self.assertTrue(result_2)

    def test_validate_class_name_is_false(self):
        validator = Validator()
        result_1 = validator.validate_class_name("name")
        result_2 = validator.validate_class_name("Name$%^&")
        result_3 = validator.validate_class_name("123Name")
        self.assertFalse(result_1)
        self.assertFalse(result_2)
        self.assertFalse(result_3)

    def test_validate_method_name_is_true(self):
        validator = Validator()
        result_1 = validator.validate_method_name("get_name")
        result_2 = validator.validate_method_name("get_1")
        result_3 = validator.validate_method_name("get")
        self.assertTrue(result_1)
        self.assertTrue(result_2)
        self.assertTrue(result_3)

    def test_validate_method_name_is_false(self):
        validator = Validator()
        result_1 = validator.validate_method_name("Get")
        result_2 = validator.validate_method_name("1_get")
        result_3 = validator.validate_method_name("get_Name")
        self.assertFalse(result_1)
        self.assertFalse(result_2)
        self.assertFalse(result_3)

    def test_get_method_name(self):
        # to be continued
        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)  # with more details
    # unittest.main()