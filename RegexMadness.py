from random import choice, randint, randrange

class FakeRegex:

    def getRandomSafeChar(self):
        """Returns an alphanumeric character not at the current index of the self.word"""
        n = self.word[self.index]
        while True:
            char = choice(self.safeChars)
            if not char == n:
                return "{}?".format(char)

    def getRandomMultiLetter(self):
        m = choice(self.multiLetterOptions)
        # if not m == self.multiLetterOptions[0] and randint(0, 20) < 15:
        #     return m.format(self.getRandomMultiLetter())
        n = self.word[self.index]
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
        return looker.format(choice(self.word[self.index:]))

    def getRandomLookBehind(self):
        looker = self.lookBehind[0]
        n = self.word[:self.index]
        while True:
            char = choice(self.safeChars)
            if not char in n:
                return looker.format(char)

    def getAheadOrBehind(self):
        # return self.getRandomLookAhead()
        if self.index - 1 < 1:
            return self.getRandomLookAhead()
        if self.index - 1 <= self.length - 1:
            return self.getRandomLookBehind()
        return self.getRandomLookAhead() if randrange(20) < 10 else self.getRandomLookBehind(self.index)

    def generate(self):
        regex = ""
        options = [self.getRandomSafeChar, self.getRandomMultiLetter, self.getAheadOrBehind]
        # options = [self.getRandomSafeChar, self.getRandomMultiLetter]
        while not self.index >= self.length:
            if randrange(15) == 1:
                regex += self.word[self.index]
                self.index += 1
                continue
            regex += choice(options)()
        return regex

    def __init__(self, word):
        self.safeChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789 "
        self.word = list(map(lambda x: x if x in self.safeChars else "\\{}".format(x), word))
        self.length = len(self.word)
        self.index = 0
        # self.unusedChars = list(filter(lambda x: not x in self.word, self.safeChars))
        self.multiLetterOptions = ["[{}]?", "(?#{})"]

        self.lookAhead = [
        "(?=.*{})"   # positive
        # "(?!{})"    # negitive
        ]

        self.lookBehind = [
        # "(?<={})"   # positive
        "(?<!{})"    # negitive
        ]

        print(self.generate())


if __name__ == '__main__':
    FakeRegex([i for i in input("Enter the word to match: ")])
