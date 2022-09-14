from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_scoreBoard()
        self.hideturtle()

    def update_scoreBoard(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreBoard()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over!', align=ALIGNMENT, font=FONT)


