class Validator:
    @staticmethod
    def validate_class_name(name):
        """
        >>> Validator.validate_class_name("ClassBuilder")
        True

        >>> Validator.validate_class_name("classBuilder")
        False
        """
        if name[0].isupper():
            return True
        else:
            return False

    # By Clement
    @staticmethod
    def validate_attribute_name(name):
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



