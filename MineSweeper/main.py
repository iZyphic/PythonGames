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


def chain_react(_):
    print(self.all_boxes.index(_))
    val = "value"

    opos = _.pos()
    oyor = _.ycor()
    oxor = _.xcor()
    _.goto(2000, 2000)
    if len(que) >= 1:
        que.pop(0)

    a_bomb = self.box_of_boxes[self.all_boxes.index(_)]["bomb"]



    '''The first box in que'''
    if self.box_of_boxes[self.all_boxes.index(_)][val] == 0:

        '''Top left box of game window'''
        if opos == (-290, 290) and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:
            #print(1)

            if self.box_of_boxes[self.all_boxes.index(_) + 1]["value"] == 0:
                if self.box_of_boxes[self.all_boxes.index(_) + 27]["value"] == 0:
                    if self.box_of_boxes[self.all_boxes.index(_) + 28]["value"] == 0:

                        self.all_boxes[self.all_boxes.index(_) + 1].goto(FAR_POS)
                        self.all_boxes[self.all_boxes.index(_) + 27].goto(FAR_POS)
                        self.all_boxes[self.all_boxes.index(_) + 28].goto(FAR_POS)
                        _ = self.all_boxes[self.all_boxes.index(_) + 1]
                        que.append(_)
                        _ = self.all_boxes[self.all_boxes.index(_) + 27]
                        que.append(_)
                        _ = self.all_boxes[self.all_boxes.index(_) + 28]
                        que.append(_)




            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 1].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_) + 1]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"]:

                self.all_boxes[self.all_boxes.index(_) + 1].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 28].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_) + 28]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"]:

                self.all_boxes[self.all_boxes.index(_) + 28].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not a_bomb:
                self.all_boxes[self.all_boxes.index(_) + 27].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_) + 27]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"]:

                self.all_boxes[self.all_boxes.index(_) + 27].goto(2000, 2000)

        #Top right box of game window
        if opos == (282.00, 290.00) and not a_bomb:
            print(2)

            if self.box_of_boxes[self.all_boxes.index(_) - 1]["value"] == 0:
                if self.box_of_boxes[self.all_boxes.index(_)+26]["value"] == 0:
                    if self.box_of_boxes[self.all_boxes.index(_)+27]["value"] == 0:
                        self.all_boxes[self.all_boxes.index(_)-1].goto(2000, 2000)
                        self.all_boxes[self.all_boxes.index(_)+26].goto(2000, 2000)
                        self.all_boxes[self.all_boxes.index(_)+27].goto(2000, 2000)
                        _ = self.all_boxes[self.all_boxes.index(_)-1]
                        que.append(_)
                        _ = self.all_boxes[self.all_boxes.index(_)+26]
                        que.append(_)
                        _ = self.all_boxes[self.all_boxes.index(_)+27]
                        que.append(_)


            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 1].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_) - 1]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 1].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 26].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_) + 26]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 26].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 27].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_) + 27]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"]:
                _ = self.all_boxes[self.all_boxes.index(_) + 27].goto(2000, 2000)

        #Bottom left box of game window
        if opos == (-290, -282) and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:
            print(3)

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 27].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_) - 27]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 27].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) - 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 26].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_) - 26]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 26].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 1].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_) + 1]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 1].goto(2000, 2000)

        #Bottom right box of game window
        if opos == (282, -282) and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:
            print(4)

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 27].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_) - 27]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 27].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) - 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 28].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)- 28]
                que.append(_)

            elif self.box_of_boxes[self.all_boxes.index(_) - 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 28].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 1].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)-1]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 1].goto(2000, 2000)

        #Left side boxes of game window

        if oxor == -290 and oyor != -282 and oyor != 290 and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:
            print(5)

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 27].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)-27]
                que.append(_)

            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 27].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) - 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 26].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)-26]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 26].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 1].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)+1]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 1].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 27].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)+27]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 27].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 28].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)+28]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 28].goto(2000, 2000)

        #Right side boxes of game window

        if oxor == 282 and oyor != -282 and oyor != 290 and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:
            print(6)
            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 27].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)-27]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 27].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) - 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 28].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)-28]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 28].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 1].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)-1]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 1].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 26].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)+26]
                que.append(_)

            elif self.box_of_boxes[self.all_boxes.index(_) + 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 26].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 27].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)+27]
                que.append(_)

            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 27].goto(2000, 2000)

        #Top boxes of game window

        if oxor != -290 and oxor != 282 and oyor == 290 and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:
            print(7)
            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 1].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)-1]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 1].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 1].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)+1]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 1].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 26].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)+26]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 26].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 27].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)+27]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 27].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 28].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)+28]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 28].goto(2000, 2000)

        #Bottom row boxes of game window

        if oyor == -282 and oxor != -290 and oxor != 282 and not self.box_of_boxes[self.all_boxes.index(_)]["bomb"]:
            print(8)
            if self.box_of_boxes[self.all_boxes.index(_) - 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 28].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)-28]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 28].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 27].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)-27]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 27].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) - 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 26].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)-26]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 26].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 1].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)-1]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 1].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 1].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)+1]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 1].goto(2000, 2000)

        #Center boxes of game window

        if 290 > oyor > -282 and -290 < oxor < 282 and not a_bomb:
            print((self.all_boxes.index(_) + 26))
            print(9)



            if self.box_of_boxes[self.all_boxes.index(_) + 28][val] == 0:
                if self.box_of_boxes[self.all_boxes.index(_)+27][val] == 0:
                    if self.box_of_boxes[self.all_boxes.index(_)+26][val] == 0:
                        if self.box_of_boxes[self.all_boxes.index(_)+1][val] == 0:
                            if self.box_of_boxes[self.all_boxes.index(_)-1][val] == 0:
                                if self.box_of_boxes[self.all_boxes.index(_)-26][val] == 0:
                                    if self.box_of_boxes[self.all_boxes.index(_)-27][val] == 0:
                                        if self.box_of_boxes[self.all_boxes.index(_)-28][val] == 0:
                                            self.all_boxes[self.all_boxes.index(_) + 28].goto(2000, 2000)
                                            self.all_boxes[self.all_boxes.index(_) + 27].goto(2000, 2000)
                                            self.all_boxes[self.all_boxes.index(_) + 26].goto(2000, 2000)
                                            self.all_boxes[self.all_boxes.index(_) + 1].goto(2000, 2000)
                                            self.all_boxes[self.all_boxes.index(_) - 1].goto(2000, 2000)
                                            self.all_boxes[self.all_boxes.index(_) - 26].goto(2000, 2000)
                                            self.all_boxes[self.all_boxes.index(_) - 27].goto(2000, 2000)
                                            self.all_boxes[self.all_boxes.index(_) - 28].goto(2000, 2000)
                                            _ = self.all_boxes[self.all_boxes.index(_) + 28]
                                            que.append(_)
                                            _ = self.all_boxes[self.all_boxes.index(_) + 27]
                                            que.append(_)
                                            _ = self.all_boxes[self.all_boxes.index(_) + 26]
                                            que.append(_)
                                            _ = self.all_boxes[self.all_boxes.index(_) + 1]
                                            que.append(_)
                                            _ = self.all_boxes[self.all_boxes.index(_) - 1]
                                            que.append(_)
                                            _ = self.all_boxes[self.all_boxes.index(_) - 26]
                                            que.append(_)
                                            _ = self.all_boxes[self.all_boxes.index(_) - 27]
                                            que.append(_)
                                            _ = self.all_boxes[self.all_boxes.index(_) - 28]
                                            que.append(_)


            if self.box_of_boxes[self.all_boxes.index(_) - 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 28].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)-28]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 28].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 27].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)-27]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 27].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) - 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 26].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)-26]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 26].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 1].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)-1]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) - 1].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 1].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)+1]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 1].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 26].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)+26]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 26].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 27].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)+27]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 27].goto(2000, 2000)

            if self.box_of_boxes[self.all_boxes.index(_) + 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 28].goto(2000, 2000)

                _ = self.all_boxes[self.all_boxes.index(_)+28]
                que.append(_)


            elif self.box_of_boxes[self.all_boxes.index(_) + 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"]:
                self.all_boxes[self.all_boxes.index(_) + 28].goto(2000, 2000)

            for _ in que:
                chain_react(_)

            que.clear()


while game_on:
    screen.update()

    def func(x, y):
        global game_on



        for _ in self.all_boxes:

            if _.xcor() in range(int(x - 10), int(x + 10)) and _.ycor() in range(int(y - 10), int(y + 10)):
                que.append(_)
                for _ in que:
                    chain_react(_)

                screen.update()


    screen.onclick(func)
    screen.mainloop()

    '''Top Left Box
    if boxes.box_of_boxes[boxes.all_boxes.index(box) - 28]["value"]:
        '''

    '''Top Middle Box
    if boxes.box_of_boxes[boxes.all_boxes.index(box) - 27]["value"]:
        '''

    '''Top Right Box
    if boxes.box_of_boxes[boxes.all_boxes.index(box) - 26]["value"]:
        '''

    '''Middle Left Box
    if boxes.box_of_boxes[boxes.all_boxes.index(box) - 1]["value"]:
        '''

    '''Middle Right Box
    if boxes.box_of_boxes[boxes.all_boxes.index(box) + 1]["value"]:
        '''

    '''Bottom Left Box
    if boxes.box_of_boxes[boxes.all_boxes.index(box) + 26]["value"]:
        '''

    '''Bottom Middle Box
    if boxes.box_of_boxes[boxes.all_boxes.index(box) + 27]["value"]:
        '''

    '''Bottom Right Box
    if boxes.box_of_boxes[boxes.all_boxes.index(box) + 28]["value"]:
        '''
