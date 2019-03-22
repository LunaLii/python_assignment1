class Validator:
    @staticmethod
    def validate_class_name(class_name):
        """
        >>> Validator.validate_class_name("ClassBuilder")
        True

        >>> Validator.validate_class_name("classBuilder")
        False
        """
        if class_name[0].isupper():
            return True
        else:
            return  False


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


    # @staticmethod
    # def validate_attribute_name(a_name):
    #     """
    #     >>> Validator.validate_class_name("name")
    #     True
    #     """
    #     if a_name.islower():
    #         return True
    #     else:
    #         return False
