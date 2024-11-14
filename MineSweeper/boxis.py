import random
from turtle import Turtle
FONT = ("Courier", 14, "normal")

class Boxes:

    def __init__(self):
        self.is_a_bomb = False
        self.box_of_boxes = []
        self.all_boxes = []
        self.create_field()
        self.search_for_bombs()
        self.assign_val()


    def assign_val(self):
        for _ in self.all_boxes:
            if self.box_of_boxes[self.all_boxes.index(_)]["value"] > 0:

                #print(self.box_of_boxes[self.all_boxes.index(_)]["value"])
                #print(self.box_of_boxes[self.all_boxes.index(_)]["bomb"])

                if not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:
                    new_x = self.all_boxes[self.all_boxes.index(_)].xcor() + 1
                    new_y = self.all_boxes[self.all_boxes.index(_)].ycor() - 12

                    num = Turtle('square')
                    num.penup()
                    num.hideturtle()
                    num.color("white")
                    num.goto(x=new_x, y=new_y)
                    num.write(self.box_of_boxes[self.all_boxes.index(_)]["value"], font=FONT, align="center")

            if self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:
                new_x = self.all_boxes[self.all_boxes.index(_)].xcor() + 1
                new_y = self.all_boxes[self.all_boxes.index(_)].ycor() - 12

                num = Turtle('square')
                num.penup()
                num.hideturtle()
                num.color("Red")
                num.goto(x=new_x, y=new_y)
                num.write('X', font=FONT, align="center")


    def create_field(self):
        self.add_row()
        self.create_mines()

    def add_row(self):
        draw = Turtle()
        draw.penup()
        draw.goto(-290, 290)
        box_id = 1
        for box in range(27):
            for x in range(27):
                is_bomb = random.randint(1,100)
                if is_bomb >= 85:
                    self.is_a_bomb = True
                else:
                    self.is_a_bomb = False

                self.box_of_boxes.append({
                    "id": box_id,
                    "column": box,
                    "row": x,
                    "bomb": self.is_a_bomb,
                    "value": 0,
                })
                box_id += 1
                self.add_box(draw)
                draw.fd(22)
            new_pos = (-290, draw.ycor() - 22)
            draw.goto(new_pos)

    def add_box(self, draw):
        new_box = Turtle('square')
        new_box.color('white')
        new_box.penup()
        new_box.goto(draw.xcor(), draw.ycor())
        self.all_boxes.append(new_box)

    def create_mines(self):
        for _ in self.all_boxes:
            if self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:
                _.color("red")

    def search_for_bombs(self):

        for _ in self.all_boxes:
            '''Top Left Box
            if self.box_of_boxes[self.all_boxes.index(_) - 28]["bomb"]:
                self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1'''

            '''Top Middle Box
            if self.box_of_boxes[self.all_boxes.index(_) - 27]["bomb"]:
                self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1'''

            '''Top Right Box
            if self.box_of_boxes[self.all_boxes.index(_) - 26]["bomb"]:
                self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1'''

            '''Middle Left Box
            if self.box_of_boxes[self.all_boxes.index(_) - 1]["bomb"]:
                self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1'''

            '''Middle Right Box
            if self.box_of_boxes[self.all_boxes.index(_) + 1]["bomb"]:
                self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1'''

            '''Bottom Left Box
            if self.box_of_boxes[self.all_boxes.index(_) + 26]["bomb"]:
                self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1'''

            '''Bottom Middle Box
            if self.box_of_boxes[self.all_boxes.index(_) + 27]["bomb"]:
                self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1'''

            '''Bottom Right Box
            if self.box_of_boxes[self.all_boxes.index(_) + 28]["bomb"]:
                self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1'''

            '''Top left box of game window'''
            if _.pos() == (-290, 290) and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:

                if self.box_of_boxes[self.all_boxes.index(_) + 1]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 28]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 27]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

            '''Top right box of game window'''
            if _.pos() == (282.00, 290.00) and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:

                if self.box_of_boxes[self.all_boxes.index(_) - 1]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 26]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 27]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

            '''Bottom left box of game window'''
            if _.pos() == (-290, -282) and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:

                if self.box_of_boxes[self.all_boxes.index(_) - 27]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) - 26]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 1]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

            '''Bottom right box of game window'''
            if _.pos() == (282, -282) and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:

                if self.box_of_boxes[self.all_boxes.index(_) - 27]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) - 28]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) - 1]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

            '''Left side boxes of game window'''

            if _.xcor() == -290 and _.ycor() != -282 and _.ycor() != 290 and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:
                if self.box_of_boxes[self.all_boxes.index(_) - 27]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) - 26]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 1]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 27]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 28]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

            '''Right side boxes of game window'''

            if _.xcor() == 282 and _.ycor() != -282 and _.ycor() != 290 and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:
                if self.box_of_boxes[self.all_boxes.index(_) - 27]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) - 28]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) - 1]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 26]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 27]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

            '''Top boxes of game window'''

            if _.xcor() != -290 and _.xcor() != 282 and _.ycor() == 290 and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:

                if self.box_of_boxes[self.all_boxes.index(_) - 1]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 1]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 26]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 27]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 28]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

            '''Bottom row boxes of game window'''

            if _.ycor() == -282 and _.xcor() != -290 and _.xcor() != 282 and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:

                if self.box_of_boxes[self.all_boxes.index(_) - 28]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) - 27]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) - 26]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) - 1]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 1]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

            '''Center boxes of game window'''

            if 290 > _.ycor() > -282 and -290 < _.xcor() < 282 and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:

                if self.box_of_boxes[self.all_boxes.index(_) - 28]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) - 27]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) - 26]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) - 1]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 1]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 26]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 27]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1

                if self.box_of_boxes[self.all_boxes.index(_) + 28]["bomb"]:
                    self.box_of_boxes[self.all_boxes.index(_)]["value"] += 1
