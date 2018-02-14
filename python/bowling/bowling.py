class BowlingGame(object):
    def __init__(self):
        self.current_frame_number = 0
        self.scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.corrections = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.rolls = [2, 2, 2, 2, 2, 2, 2, 2, 2, 3]

    def roll(self, pins):
        if pins < 0:
            raise ValueError("Can't knockdown negative pins")

        if self.current_frame_number > 9:
            raise IndexError("Can't play more than 10 frames")

        if pins > 10 or (pins + self.scores[self.current_frame_number] > 10 and self.current_frame_number < 9):
            raise ValueError("Can't knockdown more than 10 pins per frame")

        if self.current_frame_number == 9 and self.rolls[9] == 1 and \
           self.scores[9] < 20 and pins + self.scores[9] > 20:
            raise ValueError("Can't get a strike if the first roll wasn't a strike")
        self.scores[self.current_frame_number] += pins
        if self.current_frame_number >= 1 and self.corrections[self.current_frame_number - 1] > 0:
            self.scores[self.current_frame_number - 1] += pins
            self.corrections[self.current_frame_number - 1] -= 1
        if self.current_frame_number >= 2 and self.corrections[self.current_frame_number - 2] > 0:
            self.scores[self.current_frame_number - 2] += pins
            self.corrections[self.current_frame_number - 2] -= 1
        if self.scores[self.current_frame_number] == 10:
            if pins == 10:
                # strike
                self.corrections[self.current_frame_number] = 2
                if self.current_frame_number < 9:
                    self.rolls[self.current_frame_number] = 0
            else:
                # spare
                self.corrections[self.current_frame_number] = 1

        if self.rolls[self.current_frame_number] > 0:
            self.rolls[self.current_frame_number] -= 1
            if self.current_frame_number == 9 and self.scores[9] < 10 and self.rolls[9] == 1:
                # need at least a strike or spare to bowl 3 times on the 10th frame
                self.rolls[self.current_frame_number] -= 1
        if self.rolls[self.current_frame_number] == 0:
            self.current_frame_number += 1

    def score(self):
        if sum(self.rolls) > 0:
            raise IndexError("Can't score an incomplete game")

        return sum(self.scores)
