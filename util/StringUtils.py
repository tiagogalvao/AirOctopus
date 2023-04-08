class StringUtils:
    @staticmethod
    def equals_ignore_case(str1, str2):
        return str1.casefold() == str2.casefold()

    @staticmethod
    def contains_ignore_case(str1, str2):
        return str2.casefold() in str1.casefold()
