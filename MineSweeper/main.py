import turtle
from turtle import Screen
from boxis import Boxes
from turtle import Turtle
import random

FAR_POS = (2000, 2000)

screen = Screen()
screen.tracer(0)
screen.bgcolor("grey")
screen.setup(width=600, height=600)

self = Boxes()

game_on = True
que = []
send = []


def chain_react(_):


    val = "value"
    #print(self.all_boxes.index(_))

    opos = _.pos()
    oyor = _.ycor()
    oxor = _.xcor()
    send.append(_)

    a_bomb = self.box_of_boxes[self.all_boxes.index(_)]["bomb"]

    #The first box in que

    if self.box_of_boxes[self.all_boxes.index(_)][val] == 0:

        #Top left box of game window
        if opos == (-290, 290) and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:
            #print("Top left box of game window")

            if self.box_of_boxes[self.all_boxes.index(_) + 1]["value"] == 0 and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS:
                if self.box_of_boxes[self.all_boxes.index(_) + 27]["value"] == 0 and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS:
                    if self.box_of_boxes[self.all_boxes.index(_) + 28]["value"] == 0 and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS:

                        que.append(self.all_boxes[self.all_boxes.index(_) + 1])

                        que.append(self.all_boxes[self.all_boxes.index(_) + 27])

                        que.append(self.all_boxes[self.all_boxes.index(_) + 28])

            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])

            elif self.box_of_boxes[self.all_boxes.index(_) + 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 28])

            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])

        #Top right box of game window
        if opos == (282.00, 290.00) and not a_bomb:
            #print("Top right box of game window")

            if self.box_of_boxes[self.all_boxes.index(_) - 1]["value"] == 0 and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS:
                if self.box_of_boxes[self.all_boxes.index(_)+26]["value"] == 0 and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS:
                    if self.box_of_boxes[self.all_boxes.index(_)+27]["value"] == 0 and self.all_boxes[self.all_boxes.index(_+27)].pos() != FAR_POS:
                        send.append(self.all_boxes[self.all_boxes.index(_)-1])

                        send.append(self.all_boxes[self.all_boxes.index(_)+26])
                        que.append(self.all_boxes[self.all_boxes.index(_)+26])

                        send.append(self.all_boxes[self.all_boxes.index(_)+27])
                        que.append(self.all_boxes[self.all_boxes.index(_)+27])



            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                que.append(self.all_boxes[self.all_boxes.index(_) - 1])

            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])

            if self.box_of_boxes[self.all_boxes.index(_) + 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 26])
                que.append(self.all_boxes[self.all_boxes.index(_) + 26])

            elif self.box_of_boxes[self.all_boxes.index(_) + 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 26])

            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])
                que.append(self.all_boxes[self.all_boxes.index(_) + 27])

            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])

        #Bottom left box of game window
        if opos == (-290, -282) and not a_bomb:
            #print("Bottom left box of game window")

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                que.append(self.all_boxes[self.all_boxes.index(_) - 27])

            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])

            if self.box_of_boxes[self.all_boxes.index(_) - 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 26])
                que.append(self.all_boxes[self.all_boxes.index(_) - 27])

            elif self.box_of_boxes[self.all_boxes.index(_) - 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 26])

            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])
                que.append(self.all_boxes[self.all_boxes.index(_) + 1])

            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])

        #Bottom right box of game window
        if opos == (282, -282) and not a_bomb:
            #print("Bottom right box of game window")

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                que.append(self.all_boxes[self.all_boxes.index(_) - 27])

            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])

            if self.box_of_boxes[self.all_boxes.index(_) - 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 28])
                que.append(self.all_boxes[self.all_boxes.index(_) - 28])

            elif self.box_of_boxes[self.all_boxes.index(_) - 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 28])

            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                que.append(self.all_boxes[self.all_boxes.index(_) - 1])

            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])

        #Left side boxes of game window

        if oxor == -290 and oyor != -282 and oyor != 290 and not a_bomb:
            #print("Left side boxes of game window")

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                que.append(self.all_boxes[self.all_boxes.index(_) - 27])

            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])

            if self.box_of_boxes[self.all_boxes.index(_) - 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 26])
                que.append(self.all_boxes[self.all_boxes.index(_) - 26])

            elif self.box_of_boxes[self.all_boxes.index(_) - 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 26])

            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])
                que.append(self.all_boxes[self.all_boxes.index(_) + 1])

            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])

            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])
                que.append(self.all_boxes[self.all_boxes.index(_) + 27])

            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])

            if self.box_of_boxes[self.all_boxes.index(_) + 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 28])
                que.append(self.all_boxes[self.all_boxes.index(_) + 28])

            elif self.box_of_boxes[self.all_boxes.index(_) + 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 28])

        #Right side boxes of game window

        if oxor == 282 and oyor != -282 and oyor != 290 and not a_bomb:
            #print("Right side boxes of game window")
            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                que.append(self.all_boxes[self.all_boxes.index(_) - 27])

            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])

            if self.box_of_boxes[self.all_boxes.index(_) - 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 28])
                que.append(self.all_boxes[self.all_boxes.index(_) - 28])

            elif self.box_of_boxes[self.all_boxes.index(_) - 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 28])

            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                que.append(self.all_boxes[self.all_boxes.index(_) - 1])

            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])

            if self.box_of_boxes[self.all_boxes.index(_) + 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 26])
                que.append(self.all_boxes[self.all_boxes.index(_) + 26])

            elif self.box_of_boxes[self.all_boxes.index(_) + 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 26])

            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])
                que.append(self.all_boxes[self.all_boxes.index(_) + 27])

            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])

        #Top boxes of game window

        if oxor != -290 and oxor != 282 and oyor == 290 and not a_bomb:
            #print("Top boxes of game window")
            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                que.append(self.all_boxes[self.all_boxes.index(_) - 1])

            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])

            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])
                que.append(self.all_boxes[self.all_boxes.index(_) + 1])

            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])

            if self.box_of_boxes[self.all_boxes.index(_) + 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 26])
                que.append(self.all_boxes[self.all_boxes.index(_) + 26])

            elif self.box_of_boxes[self.all_boxes.index(_) + 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 26])

            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])
                que.append(self.all_boxes[self.all_boxes.index(_) + 27])

            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])

            if self.box_of_boxes[self.all_boxes.index(_) + 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 28])
                que.append(self.all_boxes[self.all_boxes.index(_) + 28])

            elif self.box_of_boxes[self.all_boxes.index(_) + 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 28])

        #Bottom row boxes of game window

        if oyor == -282 and oxor != -290 and oxor != 282 and not a_bomb:
            #print("Bottom row boxes of game window")
            if self.box_of_boxes[self.all_boxes.index(_) - 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 28])
                que.append(self.all_boxes[self.all_boxes.index(_) - 28])

            elif self.box_of_boxes[self.all_boxes.index(_) - 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 28])

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                que.append(self.all_boxes[self.all_boxes.index(_) - 27])

            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])

            if self.box_of_boxes[self.all_boxes.index(_) - 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 26])
                que.append(self.all_boxes[self.all_boxes.index(_) - 26])

            elif self.box_of_boxes[self.all_boxes.index(_) - 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 26])

            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                que.append(self.all_boxes[self.all_boxes.index(_) - 1])

            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])

            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])
                que.append(self.all_boxes[self.all_boxes.index(_) + 1])

            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])

        #Center boxes of game window

        if 290 > oyor > -282 and -290 < oxor < 282 and not a_bomb:
            #print("Center boxes of game window")



            if self.box_of_boxes[self.all_boxes.index(_) + 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS:
                if self.box_of_boxes[self.all_boxes.index(_)+27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS:
                    if self.box_of_boxes[self.all_boxes.index(_)+26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS:
                        if self.box_of_boxes[self.all_boxes.index(_)+1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS:
                            if self.box_of_boxes[self.all_boxes.index(_)-1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS:
                                if self.box_of_boxes[self.all_boxes.index(_)-26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS:
                                    if self.box_of_boxes[self.all_boxes.index(_)-27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS:
                                        if self.box_of_boxes[self.all_boxes.index(_)-28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS:

                                            send.append(self.all_boxes[self.all_boxes.index(_) + 28])
                                            que.append(self.all_boxes[self.all_boxes.index(_) + 28])

                                            send.append(self.all_boxes[self.all_boxes.index(_) + 27])
                                            que.append(self.all_boxes[self.all_boxes.index(_) + 27])

                                            send.append(self.all_boxes[self.all_boxes.index(_) + 26])
                                            que.append(self.all_boxes[self.all_boxes.index(_) + 26])

                                            send.append(self.all_boxes[self.all_boxes.index(_) + 1])
                                            que.append(self.all_boxes[self.all_boxes.index(_) + 1])

                                            send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                                            que.append(self.all_boxes[self.all_boxes.index(_) - 1])

                                            send.append(self.all_boxes[self.all_boxes.index(_) - 26])
                                            que.append(self.all_boxes[self.all_boxes.index(_) - 26])

                                            send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                                            que.append(self.all_boxes[self.all_boxes.index(_) - 27])

                                            send.append(self.all_boxes[self.all_boxes.index(_) - 28])
                                            que.append(self.all_boxes[self.all_boxes.index(_) - 28])


            if self.box_of_boxes[self.all_boxes.index(_) - 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 28])
                que.append(self.all_boxes[self.all_boxes.index(_) - 28])

            elif self.box_of_boxes[self.all_boxes.index(_) - 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 28])

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                que.append(self.all_boxes[self.all_boxes.index(_) - 27])

            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])

            if self.box_of_boxes[self.all_boxes.index(_) - 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 26])
                que.append(self.all_boxes[self.all_boxes.index(_) - 26])

            elif self.box_of_boxes[self.all_boxes.index(_) - 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 26])

            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                que.append(self.all_boxes[self.all_boxes.index(_) - 1])

            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])

            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])
                que.append(self.all_boxes[self.all_boxes.index(_) + 1])

            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])

            if self.box_of_boxes[self.all_boxes.index(_) + 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 26])
                que.append(self.all_boxes[self.all_boxes.index(_) + 26])

            elif self.box_of_boxes[self.all_boxes.index(_) + 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 26])

            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])
                que.append(self.all_boxes[self.all_boxes.index(_) + 27])

            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])

            if self.box_of_boxes[self.all_boxes.index(_) + 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 28])
                que.append(self.all_boxes[self.all_boxes.index(_) + 28])

            elif self.box_of_boxes[self.all_boxes.index(_) + 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS:
                send.append(self.all_boxes[self.all_boxes.index(_) + 28])







while game_on:
    screen.update()

    def func(x, y):
        global game_on

        reacted = 0

        for _ in self.all_boxes:

            if _.xcor() in range(int(x - 10), int(x + 10)) and _.ycor() in range(int(y - 10), int(y + 10)):
                chain_react(_)

                for box in que:
                    if reacted >= 200:
                        que.clear()
                    reacted += 1
                    chain_react(_=box)
                que.clear()

                for everybox in send:
                    everybox.goto(FAR_POS)

                screen.update()






    screen.onclick(func)
    screen.mainloop()
