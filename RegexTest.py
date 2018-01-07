from enum import Enum


class Looker:
    def next(self):
        self.index += 1
        self.current = self.string[self.index]
        return self.current

    def lookAhead(self):
        return self.string[self.index:]

    def lookBehind(self):
        return self.string[:self.index]

    def __init__(self, string):
        self.string = string
        self.index = 0
        self.current = self.string[self.index]


class BaseRegex(Enum):
    ALPHANUMERIC_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    MATCH_NUMERIC = "\d"
    MATCH_ALPHANUMERIC = "\w"
    MATCH_WHITESPACE = "\s"
    MATCH_ANY = "."



class Regex:
    def generate(self, looker=Looker):
        pass
    def __init__(self, expression=str, *allows):
        """

        :type expression: object
        """
        self.expression = expression


if __name__ == "__main__":
    pass
