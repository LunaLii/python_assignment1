import re


class Validator:
    # Luna
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

    # Clement
    @staticmethod
    def validate_attribute_name(name):
        # below is doctest
        """
        >>> Validator.validate_attribute_name("Name")
        False
        >>> Validator.validate_attribute_name("break")
        False
        >>> Validator.validate_attribute_name("attributedfjkslsdjfkdslfj;dkslfjskdlfj;dskl;fjkslfjkal;jfdkla;jfksljfkl;ajfdk;ljafkld;jfkjfakld;jfkd;fa")
        False
        >>> Validator.validate_attribute_name("a")
        False
        >>> Validator.validate_attribute_name(1)
        False
        >>> Validator.validate_attribute_name("attribute")
        True
        """
        reserved = ['and', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec',
                    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass',
                    'print', 'raise', 'return', 'try', 'while']
        if not isinstance(name, str) or name[0].isupper() or name in reserved or not 1 < len(name) < 31:
            return False
        else:
            return True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


