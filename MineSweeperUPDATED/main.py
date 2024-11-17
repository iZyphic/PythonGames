from turtle import Screen
from boxis import Boxes

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

    if _ in que:
        que.remove(_)

    '''opos is the old pos of the current box which "_" be worked on'''
    opos = _.pos()

    '''oyor is the old ycor() of the current box which "_" be worked on'''
    oyor = _.ycor()

    '''oxor is the old xcor() of the current box which "_" be worked on'''
    oxor = _.xcor()

    '''at the end of chain_react,  all boxes in the list "send" will be moved to the FAR_POS. FAR_POS = (2000, 2000)'''
    send.append(_)

    '''makes the code easier to work with'''
    a_bomb = self.box_of_boxes[self.all_boxes.index(_)]["bomb"]

    '''Current box being worked on'''
    if self.box_of_boxes[self.all_boxes.index(_)][val] == 0:

        '''If the current box is in the top left of the game window the code below will execute'''
        if opos == (-290, 290) and not a_bomb:

            if self.box_of_boxes[self.all_boxes.index(_) + 1]["value"] == 0 and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+1] in send:
                if self.box_of_boxes[self.all_boxes.index(_) + 27]["value"] == 0 and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+27] in send:
                    if self.box_of_boxes[self.all_boxes.index(_) + 28]["value"] == 0 and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+28] in send:

                        que.append(self.all_boxes[self.all_boxes.index(_) + 1])
                        que.append(self.all_boxes[self.all_boxes.index(_) + 27])
                        que.append(self.all_boxes[self.all_boxes.index(_) + 28])
                        send.append(self.all_boxes[self.all_boxes.index(_) + 1])
                        send.append(self.all_boxes[self.all_boxes.index(_) + 28])
                        send.append(self.all_boxes[self.all_boxes.index(_) + 27])

            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])

            elif self.box_of_boxes[self.all_boxes.index(_) + 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+28] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 28])

            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])

        '''If the current box is in the top right of the game window then the code below will execute'''
        if opos == (282.00, 290.00) and not a_bomb:
            #print("Top right box of game window")

            if self.box_of_boxes[self.all_boxes.index(_) - 1]["value"] == 0 and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                if self.box_of_boxes[self.all_boxes.index(_)+26]["value"] == 0 and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+26] in send:
                    if self.box_of_boxes[self.all_boxes.index(_)+27]["value"] == 0 and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+27] in send:

                        send.append(self.all_boxes[self.all_boxes.index(_)-1])
                        que.append(self.all_boxes[self.all_boxes.index(_) - 1])

                        send.append(self.all_boxes[self.all_boxes.index(_)+26])
                        que.append(self.all_boxes[self.all_boxes.index(_)+26])

                        send.append(self.all_boxes[self.all_boxes.index(_)+27])
                        que.append(self.all_boxes[self.all_boxes.index(_)+27])

            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                que.append(self.all_boxes[self.all_boxes.index(_) - 1])

            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])

            if self.box_of_boxes[self.all_boxes.index(_) + 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+26] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 26])
                que.append(self.all_boxes[self.all_boxes.index(_) + 26])

            elif self.box_of_boxes[self.all_boxes.index(_) + 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+26] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 26])

            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])
                que.append(self.all_boxes[self.all_boxes.index(_) + 27])

            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])

        ''' if the box is in the bottom left of game window the code below will execute'''
        if opos == (-290, -282) and not a_bomb:

            #print("Bottom left box of game window")

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                if self.box_of_boxes[self.all_boxes.index(_) - 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-26] in send:
                    if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+1] in send:
                        send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                        que.append(self.all_boxes[self.all_boxes.index(_) - 27])
                        send.append(self.all_boxes[self.all_boxes.index(_) - 26])
                        que.append(self.all_boxes[self.all_boxes.index(_) - 27])
                        send.append(self.all_boxes[self.all_boxes.index(_) + 1])
                        que.append(self.all_boxes[self.all_boxes.index(_) + 1])

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                que.append(self.all_boxes[self.all_boxes.index(_) - 27])

            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])

            if self.box_of_boxes[self.all_boxes.index(_) - 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-26] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 26])
                que.append(self.all_boxes[self.all_boxes.index(_) - 27])

            elif self.box_of_boxes[self.all_boxes.index(_) - 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-26] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 26])

            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])
                que.append(self.all_boxes[self.all_boxes.index(_) + 1])

            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])

        '''If the box is at the bottom right of the game window the code below will execute'''
        if opos == (282, -282) and not a_bomb:
            #print("Bottom right box of game window")

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                if self.box_of_boxes[self.all_boxes.index(_) - 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-28] in send:
                    if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                        send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                        que.append(self.all_boxes[self.all_boxes.index(_) - 27])
                        send.append(self.all_boxes[self.all_boxes.index(_) - 28])
                        que.append(self.all_boxes[self.all_boxes.index(_) - 28])
                        send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                        que.append(self.all_boxes[self.all_boxes.index(_) - 1])

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                que.append(self.all_boxes[self.all_boxes.index(_) - 27])

            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])

            if self.box_of_boxes[self.all_boxes.index(_) - 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-28] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 28])
                que.append(self.all_boxes[self.all_boxes.index(_) - 28])

            elif self.box_of_boxes[self.all_boxes.index(_) - 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-28] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 28])

            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                que.append(self.all_boxes[self.all_boxes.index(_) - 1])

            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])

        '''If the box is in the left most row of boxes the code below will execute'''
        if oxor == -290 and oyor != -282 and oyor != 290 and not a_bomb:
            #print("Left side boxes of game window")

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_) - 27]["bomb"] and self.all_boxes[self.all_boxes.index(_) - 27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_) - 27] in send:
                if self.box_of_boxes[self.all_boxes.index(_) - 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_) - 26]["bomb"] and self.all_boxes[self.all_boxes.index(_) - 26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_) - 26] in send:
                    if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_) + 1]["bomb"] and self.all_boxes[self.all_boxes.index(_) + 1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_) + 1] in send:
                        if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_) + 27]["bomb"] and self.all_boxes[self.all_boxes.index(_) + 27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_) + 27] in send:
                            if self.box_of_boxes[self.all_boxes.index(_) + 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_) + 28]["bomb"] and self.all_boxes[self.all_boxes.index(_) + 28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_) + 28] in send:
                                send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                                que.append(self.all_boxes[self.all_boxes.index(_) - 27])
                                send.append(self.all_boxes[self.all_boxes.index(_) - 26])
                                que.append(self.all_boxes[self.all_boxes.index(_) - 26])
                                send.append(self.all_boxes[self.all_boxes.index(_) + 1])
                                que.append(self.all_boxes[self.all_boxes.index(_) + 1])
                                send.append(self.all_boxes[self.all_boxes.index(_) + 27])
                                que.append(self.all_boxes[self.all_boxes.index(_) + 27])
                                send.append(self.all_boxes[self.all_boxes.index(_) + 28])
                                que.append(self.all_boxes[self.all_boxes.index(_) + 28])

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                que.append(self.all_boxes[self.all_boxes.index(_) - 27])

            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])

            if self.box_of_boxes[self.all_boxes.index(_) - 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-26] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 26])
                que.append(self.all_boxes[self.all_boxes.index(_) - 26])

            elif self.box_of_boxes[self.all_boxes.index(_) - 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-26] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 26])

            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])
                que.append(self.all_boxes[self.all_boxes.index(_) + 1])

            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])

            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])
                que.append(self.all_boxes[self.all_boxes.index(_) + 27])

            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])

            if self.box_of_boxes[self.all_boxes.index(_) + 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+28] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 28])
                que.append(self.all_boxes[self.all_boxes.index(_) + 28])

            elif self.box_of_boxes[self.all_boxes.index(_) + 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+28] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 28])

        '''If the box is in the right most row then the code below will execute'''
        if oxor == 282 and oyor != -282 and oyor != 290 and not a_bomb:
            #print("Right side boxes of game window")

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                if self.box_of_boxes[self.all_boxes.index(_) - 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-28] in send:
                    if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                        if self.box_of_boxes[self.all_boxes.index(_) + 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+26] in send:
                            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+27] in send:
                                send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                                que.append(self.all_boxes[self.all_boxes.index(_) - 27])
                                send.append(self.all_boxes[self.all_boxes.index(_) - 28])
                                que.append(self.all_boxes[self.all_boxes.index(_) - 28])
                                send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                                que.append(self.all_boxes[self.all_boxes.index(_) - 1])
                                send.append(self.all_boxes[self.all_boxes.index(_) + 26])
                                que.append(self.all_boxes[self.all_boxes.index(_) + 26])
                                send.append(self.all_boxes[self.all_boxes.index(_) + 27])
                                que.append(self.all_boxes[self.all_boxes.index(_) + 27])

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                que.append(self.all_boxes[self.all_boxes.index(_) - 27])

            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])

            if self.box_of_boxes[self.all_boxes.index(_) - 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-28] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 28])
                que.append(self.all_boxes[self.all_boxes.index(_) - 28])

            elif self.box_of_boxes[self.all_boxes.index(_) - 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-28] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 28])

            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                que.append(self.all_boxes[self.all_boxes.index(_) - 1])

            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])

            if self.box_of_boxes[self.all_boxes.index(_) + 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+26] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 26])
                que.append(self.all_boxes[self.all_boxes.index(_) + 26])

            elif self.box_of_boxes[self.all_boxes.index(_) + 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+26] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 26])

            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])
                que.append(self.all_boxes[self.all_boxes.index(_) + 27])

            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])

        '''If the box is in the top row of game window the code below will execute'''
        if oxor != -290 and oxor != 282 and oyor == 290 and not a_bomb:
            #print("Top boxes of game window")

            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+1] in send:
                    if self.box_of_boxes[self.all_boxes.index(_) + 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+26] in send:
                        if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+27] in send:
                            if self.box_of_boxes[self.all_boxes.index(_) + 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+28] in send:
                                send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                                que.append(self.all_boxes[self.all_boxes.index(_) - 1])
                                send.append(self.all_boxes[self.all_boxes.index(_) + 1])
                                que.append(self.all_boxes[self.all_boxes.index(_) + 1])
                                send.append(self.all_boxes[self.all_boxes.index(_) + 26])
                                que.append(self.all_boxes[self.all_boxes.index(_) + 26])
                                send.append(self.all_boxes[self.all_boxes.index(_) + 27])
                                que.append(self.all_boxes[self.all_boxes.index(_) + 27])
                                send.append(self.all_boxes[self.all_boxes.index(_) + 28])
                                que.append(self.all_boxes[self.all_boxes.index(_) + 28])

            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                que.append(self.all_boxes[self.all_boxes.index(_) - 1])

            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])

            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])
                que.append(self.all_boxes[self.all_boxes.index(_) + 1])

            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])

            if self.box_of_boxes[self.all_boxes.index(_) + 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+26] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 26])
                que.append(self.all_boxes[self.all_boxes.index(_) + 26])

            elif self.box_of_boxes[self.all_boxes.index(_) + 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+26] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 26])

            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])
                que.append(self.all_boxes[self.all_boxes.index(_) + 27])

            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])

            if self.box_of_boxes[self.all_boxes.index(_) + 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+28] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 28])
                que.append(self.all_boxes[self.all_boxes.index(_) + 28])

            elif self.box_of_boxes[self.all_boxes.index(_) + 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+28] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 28])

        '''If the box is in the bottom row of the game window the code below will execute'''
        if oyor == -282 and oxor != -290 and oxor != 282 and not a_bomb:
            #print("Bottom row boxes of game window")
            if self.box_of_boxes[self.all_boxes.index(_) - 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-28] in send:
                if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                    if self.box_of_boxes[self.all_boxes.index(_) - 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-26] in send:
                        if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+1] in send:
                                send.append(self.all_boxes[self.all_boxes.index(_) - 28])
                                que.append(self.all_boxes[self.all_boxes.index(_) - 28])

                                send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                                que.append(self.all_boxes[self.all_boxes.index(_) - 27])

                                send.append(self.all_boxes[self.all_boxes.index(_) - 26])
                                que.append(self.all_boxes[self.all_boxes.index(_) - 26])

                                send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                                que.append(self.all_boxes[self.all_boxes.index(_) - 1])

                                send.append(self.all_boxes[self.all_boxes.index(_) + 1])
                                que.append(self.all_boxes[self.all_boxes.index(_) + 1])

            if self.box_of_boxes[self.all_boxes.index(_) - 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-28] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 28])
                que.append(self.all_boxes[self.all_boxes.index(_) - 28])

            elif self.box_of_boxes[self.all_boxes.index(_) - 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-28] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 28])

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                que.append(self.all_boxes[self.all_boxes.index(_) - 27])

            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])

            if self.box_of_boxes[self.all_boxes.index(_) - 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-26] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 26])
                que.append(self.all_boxes[self.all_boxes.index(_) - 26])

            elif self.box_of_boxes[self.all_boxes.index(_) - 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-26] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 26])

            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                que.append(self.all_boxes[self.all_boxes.index(_) - 1])

            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])

            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])
                que.append(self.all_boxes[self.all_boxes.index(_) + 1])

            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])

        '''If the box is not in the left, right, top ,bottom, and the corners the code below will execute'''
        if 290 > oyor > -282 and -290 < oxor < 282 and not a_bomb:
            #print("Center boxes of game window")

            if self.box_of_boxes[self.all_boxes.index(_) + 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+28] in send:
                if self.box_of_boxes[self.all_boxes.index(_)+27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+27] in send:
                    if self.box_of_boxes[self.all_boxes.index(_)+26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+26] in send:
                        if self.box_of_boxes[self.all_boxes.index(_)+1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+1] in send:
                            if self.box_of_boxes[self.all_boxes.index(_)-1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                                if self.box_of_boxes[self.all_boxes.index(_)-26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-26] in send:
                                    if self.box_of_boxes[self.all_boxes.index(_)-27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                                        if self.box_of_boxes[self.all_boxes.index(_)-28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-28] in send:

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

            if self.box_of_boxes[self.all_boxes.index(_) - 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-28] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 28])
                que.append(self.all_boxes[self.all_boxes.index(_) - 28])

            elif self.box_of_boxes[self.all_boxes.index(_) - 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-28]["bomb"] and self.all_boxes[self.all_boxes.index(_)-28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-28] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 28])

            if self.box_of_boxes[self.all_boxes.index(_) - 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])
                que.append(self.all_boxes[self.all_boxes.index(_) - 27])

            elif self.box_of_boxes[self.all_boxes.index(_) - 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-27]["bomb"] and self.all_boxes[self.all_boxes.index(_)-27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 27])

            if self.box_of_boxes[self.all_boxes.index(_) - 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-26] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 26])
                que.append(self.all_boxes[self.all_boxes.index(_) - 26])

            elif self.box_of_boxes[self.all_boxes.index(_) - 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-26]["bomb"] and self.all_boxes[self.all_boxes.index(_)-26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-26] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 26])

            if self.box_of_boxes[self.all_boxes.index(_) - 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])
                que.append(self.all_boxes[self.all_boxes.index(_) - 1])

            elif self.box_of_boxes[self.all_boxes.index(_) - 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)-1]["bomb"] and self.all_boxes[self.all_boxes.index(_)-1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)-1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) - 1])

            if self.box_of_boxes[self.all_boxes.index(_) + 1][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])
                que.append(self.all_boxes[self.all_boxes.index(_) + 1])

            elif self.box_of_boxes[self.all_boxes.index(_) + 1][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+1]["bomb"] and self.all_boxes[self.all_boxes.index(_)+1].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+1] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 1])

            if self.box_of_boxes[self.all_boxes.index(_) + 26][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+26] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 26])
                que.append(self.all_boxes[self.all_boxes.index(_) + 26])

            elif self.box_of_boxes[self.all_boxes.index(_) + 26][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+26]["bomb"] and self.all_boxes[self.all_boxes.index(_)+26].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+26] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 26])

            if self.box_of_boxes[self.all_boxes.index(_) + 27][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])
                que.append(self.all_boxes[self.all_boxes.index(_) + 27])

            elif self.box_of_boxes[self.all_boxes.index(_) + 27][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+27]["bomb"] and self.all_boxes[self.all_boxes.index(_)+27].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+27] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 27])

            if self.box_of_boxes[self.all_boxes.index(_) + 28][val] == 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+28] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 28])
                que.append(self.all_boxes[self.all_boxes.index(_) + 28])

            elif self.box_of_boxes[self.all_boxes.index(_) + 28][val] > 0 and not self.box_of_boxes[self.all_boxes.index(_)+28]["bomb"] and self.all_boxes[self.all_boxes.index(_)+28].pos() != FAR_POS and not self.all_boxes[self.all_boxes.index(_)+28] in send:
                send.append(self.all_boxes[self.all_boxes.index(_) + 28])


while game_on:
    screen.update()

    def logic(x, y):
        global game_on

        for _ in self.all_boxes:

            if _.xcor() in range(int(x - 10), int(x + 10)) and _.ycor() in range(int(y - 10), int(y + 10)):
                chain_react(_)

                for box in que:
                    chain_react(_=box)
                que.clear()

                for box in send:
                    box.goto(FAR_POS)
                screen.update()

    '''When the player clicks the function "logic" will trigger'''
    screen.onclick(logic)
    
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
