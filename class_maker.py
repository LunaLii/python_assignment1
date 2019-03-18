from attribute_maker import AttributeMaker
from method_maker import MethodMaker
from relationship_maker import RelationshipMaker
class ClassMaker:

    def __init__(self, class_name, new_attributes, new_methods, new_relationship):
        self.name = class_name
        self.attributes = new_attributes
        self.methods = new_methods
        self.relationships = new_relationship
        self.all_my_attributes = []
        self.all_my_methods = []
        self.all_my_relationships = []

    def add_class_attributes(self):
        for an_attribute in self.attributes:
            new_a_name = an_attribute.split(":")[0]
            new_a_return = an_attribute.split(":")[1]
            new_a = AttributeMaker(new_a_name, new_a_return)
            self.all_my_attributes.append(new_a)

    def add_class_methods(self):
        for a_method in self.methods:
            new_m_name = a_method.split("(")[0]
            new_m_return = a_method.split("(")[1]
            if new_m_name != "  __init__":
                new_m = MethodMaker(new_m_name, new_m_return)
                self.all_my_methods.append(new_m)

    def add_class_relationships(self):
        for a_relationship in self.relationships:
            r_class_name = a_relationship.split(" ")
            first_c_name = r_class_name[0]
            second_c_name = r_class_name[-1]
            if first_c_name == self.name:
                the_relationship = RelationshipMaker(second_c_name)
                self.all_my_relationships.append(the_relationship)

    def print_class(self):
        print("class", self.name, ":", end = "")
        print("\n\n", "   def __init__ (self):")
        for item in self.all_my_relationships:
            print(item)
        for x in self.all_my_attributes:
            print(x)
        print("\n")
        for x in self.all_my_methods:
            print(x)
        print("\n\n")