import random

class Game:
    def __init__(self):
        self.computer = []
        self.player = []
        self.chosen = []

    def add_sentence(self, sentence, filename):
        fd = open(filename, "a")
        fd.write(sentence)
        fd.write("\n")
        fd.close()

    def get_sentence(self, filename, chosen):
        fd = open(filename, "r")
        line = fd.readline()
        options = []
        while len(line) > 0:
            options.append(line)
            line = fd.readline()

        self.computer = random.choice(options)
        self.player = []
        for i in range(len(self.computer)):
            if self.computer[i] == " ":
                self.player.append(" ")
            else:
                self.player.append("_")
        token = self.computer.split(" ")
        for i in range(len(self.computer)):
            if i == 0:
                '''First letter in the sentence'''
                self.player = self.computer[i]
                if self.computer[i] not in chosen:
                    chosen.append(self.computer[i])
            elif i == len(self.computer) - 1:
                '''Last letter in the sentence'''
                if self.computer[i] not in chosen:
                    chosen.append(self.computer[i])
                self.player[i] = self.computer[i]
            elif self.computer[i + 1] == " ":
                '''Last letter in a word '''
                if self.computer[i] not in chosen:
                    chosen.append(self.computer[i])
                self.player[i] = self.computer[i]
            elif self.computer[i - 1] == " ":
                '''First letter in a word'''
                if self.computer[i] not in chosen:
                    chosen.append(self.computer[i])
                self.player[i] = self.computer[i]
        # return chosen
    def wrong_move(self):
        pass
    def process_letters(self, chosen):
        pass
        for word in str(self.computer):
            for i in range(len(word)):
                if word[i] not in chosen:
                    chosen.append(word[i])
    def __str__(self):
        return "Current status: ", str(self.player), "\nLetters tried: ", str(self.chosen)

