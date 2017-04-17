from random import choice, randint

class FakeRegex:

    def getRandomChar(self):
        return "{}?".format(choice(self.unusedChars))

    def getRandomMultiLetter(self):
        m = choice(self.multiLetterOptions)
        # if not m == self.multiLetterOptions[0] and randint(0, 20) < 15:
        #     return m.format(self.getRandomMultiLetter())
        chars = ""
        for i in range(randint(1, 10)):
            chars += choice(self.unusedChars)

        return m.format(chars)

    def getRandomLookAhead(self):
        option = choice(self.lookAhead)
        if option == self.lookAhead[0]:     # positive lookAhead
            return option.format(choice(self.word))
        else:                               # negitive lookAhead
            return option.format(choice(self.unusedChars))

    def getRandomLookBehind(self):
        option = choice(self.lookBehind)
        if option == self.lookBehind[0]:     # positive lookBehind
            return option.format(choice(self.word))
        else:                                # negitive lookBehind
            return option.format(choice(self.unusedChars))

    def insertMatch(self):
        self.matchInserted = True
        result = "".join(self.word)
        self.word.pop()
        return result

    def getAheadOrBehind(self):
        if self.matchInserted:
            return self.getRandomLookBehind()
        return self.getRandomLookAhead()

    def generate(self):
        # options = [self.getRandomChar, self.getRandomMultiLetter, self.getAheadOrBehind]
        options = [self.getRandomMultiLetter, self.getAheadOrBehind]
        for i in range(101):
            if i == 50:
                self.regex = self.regex + self.insertMatch()
                # print(self.insertMatch())
                continue
            self.regex = self.regex + choice(options)()
            # print(choice(options)())
        return self.regex

    def __init__(self, word):
        self.regex = ""
        self.word = word
        self.chars = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"]
        self.unusedChars = list(filter(lambda x: not x in self.word, self.chars))
        # self.multiLetterOptions = ["[{}]?", "(?#{})"]
        self.multiLetterOptions = ["(?#{})"]

        self.lookAhead = [
        "(?=.*{})"   # positive
        # "(?!{})"    # negitive
        ]

        self.lookBehind = [
        # "(?<={})"   # positive
        "(?<!{})"    # negitive
        ]

        self.matchInserted = False

        # print(self.getRandomChar())
        # print(self.getRandomMultiLetter())
        # print(self.getRandomLookAhead())
        # print(self.getRandomLookBehind())
        print(self.generate())


if __name__ == '__main__':
    FakeRegex([i for i in input("Enter the word to match: ")])
