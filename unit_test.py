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

    def test_read_word_file(self):
        print_class = PrintClass()
        actual_result = print_class.read_word_file("test2.docx")
        expected = ["@startuml\n", "ToyBox *-- Toy\n", "\n", "class ToyBox {\n", "    name : String\n", "}\n", "\n", "class Toy {\n", "}\n",
                    "@enduml\n"]
        self.assertEqual(expected,actual_result)

    def test_get_method_name(self):
        print_class = PrintClass()
        class_item = print_class.class_handler("test.docx")
        actual_one = print_class.get_methods(class_item[0])
        expected_one = ["add_toy", "get_toy"]
        actual_two = print_class.get_methods(class_item[1])
        expected_two = ["__str__"]
        self.assertEqual(expected_one, actual_one)
        self.assertEqual(expected_two, actual_two)

    # def test_load_file_wrong_type_exception(self):
    #     c = Controller()
    #     # with self.assertRaises(NameError) as context:
    #     #     c.load_file("uml.csv")
    #     # self.assertTrue("Incorrect file type, please see help load" in str(context.exception))
    #     self.assertRaises(FileNotFoundError,c.load_file, "C:\\Users\Luna\ICT\\uml.docx")






if __name__ == '__main__':
    unittest.main(verbosity=2)  # with more details
    # unittest.main()