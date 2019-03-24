import re


class Validator:
    @staticmethod
    def validate_class_name(class_name):
        """
        >>> Validator.validate_class_name("ClassBuilder")
        True
        >>> Validator.validate_class_name("ClassName123")
        True
        >>> Validator.validate_class_name("classBuilder")
        False
        >>> Validator.validate_class_name("C!#Name")
        False
        >>> Validator.validate_class_name("ClassName>")
        False
        >>> Validator.validate_class_name("1ClassName>")
        False
        """
        regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')
        if class_name[0].isupper() and regex.search(class_name) is None:
            return True
        else:
            return False


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


