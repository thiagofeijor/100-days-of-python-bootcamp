from turtle import Turtle

BLOCKS = [
    {
        "color": "red",
        "column": -280,
    },
    {
        "color": "orange",
        "column": -200,
    },
    {
        "color": "yellow",
        "column": -120,
    },
    {
        "color": "yellow",
        "column": -40,
    },
    {
        "color": "green",
        "column": 40,
    },
    {
        "color": "green",
        "column": 120,
    },
    {
        "color": "blue",
        "column": 200,
    },
    {
        "color": "purple",
        "column": 280,
    },
]

class BlockManager:

    def __init__(self):
        self.all_blocks = []
        for i in range(0, 8):
            self.create_car(i)

    def start_game(self):
        for blck in self.all_blocks:
            blck.showturtle()

    def hit_block(self, block):
        block.hideturtle()

    def hit_all(self):
        blocks = [blck for blck in self.all_blocks if blck.isvisible()]
        return len(blocks) == 0

    def create_car(self, column):
        new_block = Turtle("square")
        new_block.shapesize(stretch_wid=1, stretch_len=3)
        new_block.penup()
        new_block.color(BLOCKS[column]["color"])
        new_block.goto(BLOCKS[column]["column"], 240)
        self.all_blocks.append(new_block)
