from random import choice, randint, randrange
from Builders import


class FakeRegex:
    def getRandomSafeChar(self):
        """Returns an alphanumeric character not at the current index of the self.text"""
        n = self.text[self.index]
        while True:
            char = choice(self.safeChars)
            if not char == n:
                return "{}?".format(char)

    def getRandomMultiLetter(self):
        m = choice(self.multiLetterOptions)
        n = self.text[self.index]
        chars = ""
        for i in range(randint(1, 10)):
            while True:
                char = choice(self.safeChars)
                if not char == n:
                    chars += char
                    break

        return m.format(chars)

    def getRandomLookAhead(self):
        looker = self.lookAhead[0]
        return looker.format(choice(self.text[self.index:]))

    def getRandomLookBehind(self):
        looker = self.lookBehind[0]

        chars = set(self.safeChars) - set(filter(lambda x: x.isalnum() or x == " ", self.text[:self.index]))
        return looker.format(choice(list(chars)))

    def getAheadOrBehind(self):
        # return self.getRandomLookAhead()
        if self.index - 1 < 1:
            return self.getRandomLookAhead()
        if self.index - 1 <= self.length - 1:
            return self.getRandomLookBehind()
        return self.getRandomLookAhead() if randrange(20) < 10 else self.getRandomLookBehind(self.index)

    def generate(self, oneInX=15):
        regex = ""
        options = [self.getRandomSafeChar, self.getRandomMultiLetter, self.getAheadOrBehind]
        # options = [self.getRandomSafeChar, self.getRandomMultiLetter]
        while not self.index >= self.length:
            if randrange(oneInX) == 0:
                regex += self.text[self.index]
                self.index += 1
                continue
            regex += choice(options)()
        return regex

    def setText(self, text):
        self.text = list(map(lambda x: x if x in self.safeChars else "\\{}".format(x), text))
        self.length = len(self.text)
        self.index = 0
        return self

    def __init__(self):
        self.safeChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789 "
        self.multiLetterOptions = ["[{}]?", "(?#{})"]

        self.lookAhead = [
        "(?=.*{})"   # positive
        # "(?!{})"    # negitive
        ]

        self.lookBehind = [
        # "(?<={})"   # positive
        "(?<!{})"    # negitive
        ]


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("text", nargs="*", help="The text to regexify")
    parser.add_argument("-c", type=int, help="Chance of random useless regex (higher is longer)")

    args = vars(parser.parse_args())
    chance = args["c"] if args["c"] else 15

    print(FakeRegex().setText(" ".join(args["text"])).generate(chance))
