add_library('sound')
# add_library('Minim')
# minim = Minim(this)
import random

import os
path = os.getcwd()

def distance(x1, y1, x2, y2):
    return((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


class Tile:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.status = 0
        self.val = 0

class Board:

    def __init__(self):
        self.numRows = screenHeight / cellWidth
        self.numCols = screenWidth / cellWidth
        self.board1 = []
        self.police = []
        self.img = loadImage(path + "/image" + str(level) + ".png")
        self.moneyimg = loadImage(path + '/money' + str(level) + ".png")
        self.populateBoard()

    def makeBarrier(self, r, c):
        self.getTile(r, c).status = 1
        self.getTile(r, c).val = 1

    def getTile(self, r, c):
        for tile in self.board1:
            if r == tile.row and c == tile.col:
                return tile
        return Tile(-1, -1)

    def populateBoard(self):
        for r in range(-1, self.numRows + 1):
            for c in range(-1, self.numCols + 1):
                self.board1.append(Tile(r, c))

        stage = open(path + '/level' + str(level))

        for line in stage:
            line = line.strip().split(',')
            if line[0] == 'b':
                self.makeBarrier(int(line[1]), int(line[2]))
            if line[0] == 'p':
                # line 1 and 2 are coordinates of initial pos, line 3,4 are
                # paths of image and imagev
                self.police.append(
                    Police(int(line[1]), int(line[2]), str(line[3]), str(line[4])))
            if line[0] == 'm':
                self.music = 

        for row in range(-1, self.numRows + 1):
            self.makeBarrier(row, -1)
            self.makeBarrier(row, self.numCols)

        for col in range(-1, self.numCols + 1):
            self.makeBarrier(-1, col)
            self.makeBarrier(self.numRows, col)

    # def display(self):
    #     for r in range(self.numRows):
    #         for c in range(self.numCols):
    #             if self.getTile(r, c).status == 1:
    #                 fill(225, 225, 225)
    #             elif self.getTile(r, c).status == 0:
    #                 fill(0)
    # rect(self.getTile(r, c).col * cellWidth, self.getTile(r,
    # c).row*cellWidth, cellWidth, cellWidth)
    #             if self.getTile(r, c).val == 0:
    #                 fill(0, 0, 255)
    #                 rect(self.getTile(r, c).col * cellWidth,
    #                      self.getTile(r, c).row * cellWidth, 10, 10)

    def display(self):
        for r in range(self.numRows):
            for c in range(self.numCols):
                if self.getTile(r, c).val == 0:
                    image(self.moneyimg, self.getTile(r, c).col *
                          cellWidth + 5, self.getTile(r, c).row * cellWidth + 30)
        textSize(30)
        text("Player 1: " + str(game.player1.score), 100, 675)
        text("Player 2: " + str(game.player2.score), 700, 675)

        for i in range(game.player1.lives):
            image(game.player1.imgv, 350 + i * cellWidth, 653,
                  cellWidth / 2, cellWidth / 2, 0, 50, 50, 0)
        for i in range(game.player2.lives):
            image(game.player2.imgv, 950 + i * cellWidth, 653,
                  cellWidth / 2, cellWidth / 2, 0, 50, 50, 0)

class Creatures:

    def __init__(self, r, c):
        self.score = 0
        self.r = r
        self.c = c
        self.x = cellWidth * self.c
        self.y = cellWidth * self.r
        self.score = 0
        self.lives = 3


class Player1(Creatures):

    def __init__(self, r, c):
        Creatures.__init__(self, r, c)
        self.keyInput = {UP: False, DOWN: False, RIGHT: False, LEFT: False}
        self.img = loadImage(path + "/car1.png")
        self.imgv = loadImage(path + "/car1v.png")
        self.f = 0

        self.lastV = 1

    def update(self):
        if self.keyInput[LEFT] and self.collision() == False and not (self.c - 1 == game.player2.c and self.r == game.player2.r):
            self.c -= 1
            self.lastV = 1

        elif self.keyInput[RIGHT] and self.collision() == False and not (self.c + 1 == game.player2.c and self.r == game.player2.r):
            self.c += 1
            self.lastV = 2

        elif self.keyInput[UP] and self.collision() == False and not (self.r - 1 == game.player2.r and self.c == game.player2.c):
            self.r -= 1
            self.lastV = 3

        elif self.keyInput[DOWN] and self.collision() == False and not (self.r + 1 == game.player2.r and self.c == game.player2.c):
            self.r += 1
            self.lastV = 4

        self.x = cellWidth * self.c
        self.y = cellWidth * self.r
        if game.board.getTile(self.r, self.c).val == 0:
            self.score += 100
            game.board.getTile(self.r, self.c).val = 2

    def collision(self):
        if self.keyInput[UP]:
            if game.board.getTile(self.r - 1, self.c).status == 1:
                return True
        elif self.keyInput[DOWN]:
            if game.board.getTile(self.r + 1, self.c).status == 1:
                return True
        elif self.keyInput[RIGHT]:
            if game.board.getTile(self.r, self.c + 1).status == 1:
                return True
        elif self.keyInput[LEFT]:
            if game.board.getTile(self.r, self.c - 1).status == 1:
                return True
        return False

    def display(self):
        self.f = (self.f + 1) % 6
        if self.f == 0:
            self.update()
        fill(0)
        stroke(255, 0, 0)

        if self.lastV == 1:
            # rect(self.x, self.y, cellWidth, cellWidth)
            image(self.img, self.x, self.y, cellWidth,
                  cellWidth, 0, 0, 50, 50)
        elif self.lastV == 2:
            # rect(self.x, self.y, cellWidth, cellWidth)
            image(self.img, self.x, self.y, cellWidth,
                  cellWidth, 50, 0, 0, 50)
        elif self.lastV == 3:
            # rect(self.x, self.y, cellWidth, cellWidth)
            image(self.imgv, self.x, self.y,
                  cellWidth, cellWidth, 0, 50, 50, 0)
        elif self.lastV == 4:
            # rect(self.x, self.y, cellWidth, cellWidth)
            image(self.imgv, self.x, self.y,
                  cellWidth, cellWidth, 0, 0, 50, 50)


class Player2(Creatures):

    def __init__(self, r, c):
        Creatures.__init__(self, r, c)
        self.keyInput = {'W': False, 'S': False, 'D': False, 'A': False}
        self.img = loadImage(path + "/car2.png")
        self.imgv = loadImage(path + "/car2v.png")
        self.f = 0

        self.lastV = 1

    def update(self):
        if self.keyInput['A'] and self.collision() == False and not (self.c - 1 == game.player1.c and self.r == game.player1.r):
            self.c -= 1
            self.lastV = 1

        elif self.keyInput['D'] and self.collision() == False and not (self.c + 1 == game.player1.c and self.r == game.player1.r):
            self.c += 1
            self.lastV = 2

        elif self.keyInput['W'] and self.collision() == False and not (self.r - 1 == game.player1.r and self.c == game.player1.c):
            self.r -= 1
            self.lastV = 3

        elif self.keyInput['S'] and self.collision() == False and not (self.r + 1 == game.player1.r and self.c == game.player1.c):
            self.r += 1
            self.lastV = 4

        self.x = cellWidth * self.c
        self.y = cellWidth * self.r

        if game.board.getTile(self.r, self.c).val == 0:
            self.score += 100
            game.board.getTile(self.r, self.c).val = 2

    def collision(self):
        if self.keyInput['W']:
            if game.board.getTile(self.r - 1, self.c).status == 1:
                return True
        elif self.keyInput['S']:
            if game.board.getTile(self.r + 1, self.c).status == 1:
                return True
        elif self.keyInput['D']:
            if game.board.getTile(self.r, self.c + 1).status == 1:
                return True
        elif self.keyInput['A']:
            if game.board.getTile(self.r, self.c - 1).status == 1:
                return True
        return False

    def display(self):
        self.f = (self.f + 1) % 6
        if self.f == 0:
            self.update()
        # fill(0)
        # stroke(255, 0, 0)

        if self.lastV == 1:
            # rect(self.x, self.y, cellWidth, cellWidth)
            image(self.img, self.x, self.y, cellWidth,
                  cellWidth, 0, 0, 50, 50)
        elif self.lastV == 2:
            # rect(self.x, self.y, cellWidth, cellWidth)
            image(self.img, self.x, self.y, cellWidth,
                  cellWidth, 50, 0, 0, 50)
        elif self.lastV == 3:
            # rect(self.x, self.y, cellWidth, cellWidth)
            image(self.imgv, self.x, self.y,
                  cellWidth, cellWidth, 0, 50, 50, 0)
        elif self.lastV == 4:
            # rect(self.x, self.y, cellWidth, cellWidth)
            image(self.imgv, self.x, self.y,
                  cellWidth, cellWidth, 0, 0, 50, 50)


class Police(Creatures):

    def __init__(self, r, c, img, imgv):
        Creatures.__init__(self, r, c)
        self.img = loadImage(path + img)
        self.imgv = loadImage(path + imgv)
        self.lastV = 1
        self.rand_dir = 1
        self.f = 0

    def update(self):

        if self.collision() == True:
            self.rand_dir = random.randint(1, 4)

            if self.rand_dir == 1:
                if self.collision() == False:
                    game.board.getTile(self.r, self.c).status = 0
                    self.c -= 1
                    self.lastV = 1
                    game.board.getTile(self.r, self.c).status = 1
            elif self.rand_dir == 2:
                if self.collision() == False:
                    game.board.getTile(self.r, self.c).status = 0
                    self.c += 1
                    self.lastV = 2
                    game.board.getTile(self.r, self.c).status = 1
            elif self.rand_dir == 3:
                if self.collision() == False:
                    game.board.getTile(self.r, self.c).status = 0
                    self.r -= 1
                    self.lastV = 3
                    game.board.getTile(self.r, self.c).status = 1
            elif self.rand_dir == 4:
                if self.collision() == False:
                    game.board.getTile(self.r, self.c).status = 0
                    self.r += 1
                    self.lastV = 4
                    game.board.getTile(self.r, self.c).status = 1
        else:
            if self.rand_dir == 1:
                if self.collision() == False:
                    game.board.getTile(self.r, self.c).status = 0
                    self.c -= 1
                    self.lastV = 1
                    game.board.getTile(self.r, self.c).status = 1
            elif self.rand_dir == 2:
                if self.collision() == False:
                    game.board.getTile(self.r, self.c).status = 0
                    self.c += 1
                    self.lastV = 2
                    game.board.getTile(self.r, self.c).status = 1
            elif self.rand_dir == 3:
                if self.collision() == False:
                    game.board.getTile(self.r, self.c).status = 0
                    self.r -= 1
                    self.lastV = 3
                    game.board.getTile(self.r, self.c).status = 1
            elif self.rand_dir == 4:
                if self.collision() == False:
                    game.board.getTile(self.r, self.c).status = 0
                    self.r += 1
                    self.lastV = 4
                    game.board.getTile(self.r, self.c).status = 1

        self.x = cellWidth * self.c
        self.y = cellWidth * self.r

    def collision(self):
        if self.rand_dir == 4:
            if game.board.getTile(self.r + 1, self.c).status == 1:
                return True
        elif self.rand_dir == 3:
            if game.board.getTile(self.r - 1, self.c).status == 1:
                return True
        elif self.rand_dir == 2:
            if game.board.getTile(self.r, self.c + 1).status == 1:
                return True
        elif self.rand_dir == 1:
            if game.board.getTile(self.r, self.c - 1).status == 1:
                return True
        return False

    def display(self):
        self.f = (self.f + 1) % (12 - level * 2)
        if self.f == 0:
            self.update()
        # fill(0)
        # stroke(255, 0, 0)

        if self.lastV == 1:
            # rect(self.x, self.y, cellWidth, cellWidth)
            image(self.img, self.x, self.y, cellWidth,
                  cellWidth, 50, 0, 0, 50)
        elif self.lastV == 2:
            # rect(self.x, self.y, cellWidth, cellWidth)
            image(self.img, self.x, self.y, cellWidth,
                  cellWidth, 0, 0, 50, 50)

        elif self.lastV == 3:
            # rect(self.x, self.y, cellWidth, cellWidth)
            image(self.imgv, self.x, self.y,
                  cellWidth, cellWidth, 0, 0, 50, 50)

        elif self.lastV == 4:
            # rect(self.x, self.y, cellWidth, cellWidth)
            image(self.imgv, self.x, self.y,
                  cellWidth, cellWidth, 0, 50, 50, 0)


class Game:

    def __init__(self):
        self.player1 = Player1(xcoord1, ycoord1)
        self.player2 = Player2(xcoord2, ycoord2)
        self.imgMenu = loadImage(path + "/menu.jpg")
        self.imgKeyControls = loadImage(path + "/controls.png")
        self.imgScore = loadImage(path + "/score.jpg")
        self.board = Board()
        self.win = False
        self.loose = False
        self.winindent = None
        self.input1 = False
        self.input2 = False
        self.txt1 = ''
        self.txt2 = ''
        self.state = 'menu'

        self.clicked1 = 0
        self.clicked2 = 0

    def display(self):
        self.mainLogic()
        image(self.board.img, 0, 0)
        self.board.display()
        self.player1.display()
        self.player2.display()
        for p in self.board.police:
            p.display()

    def mainLogic(self):
        global level, xcoord1, ycoord1, xcoord2, ycoord2

        self.winCheck()
        self.busted()
               #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
               #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if self.win == True and level < 3:
            level += 1
            self.win = False
            if level == 3:
                xcoord1 = 10
                ycoord1 = 8
                xcoord2 = 10
                ycoord2 = 10
            self.player1.r = xcoord1
            self.player1.c = ycoord1
            self.player2.r = xcoord2
            self.player2.c = ycoord2

            self.board.__init__()
                   #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        elif self.win == True:
            # (set the mode to score)
            if self.player1.score > self.player2.score:
                self.winindent = 'Player1'
            elif self.player2.score > self.player1.score:
                self.winindent = 'Player2'
            else:
                self.winindent = 'Tie'

            self.state = 'score'
            level = 1

        if self.loose == True:
            self.state = 'score'
            level = 1
            # compare and display the scores

    def winCheck(self):
        self.win = True
        for r in range(self.board.numRows):
            for c in range(self.board.numCols):
                if self.board.getTile(r, c).val == 0:
                    self.win = False

        if self.player1.lives < 0:
            self.loose = True
            self.winindent = 'Player2'
            self.player1.score = 0

        elif self.player2.lives < 0:
            self.loose = True
            self.winindent = 'Player1'
            self.player2.score = 0

    def busted(self):
        for p in self.board.police:
            if self.player1.c == p.c and self.player1.r == p.r:
                self.player1.lives -= 1
                self.player1.r = xcoord1
                self.player1.c = ycoord1

                # remove image for live
            elif self.player2.c == p.c and self.player2.r == p.r:
                self.player2.lives -= 1
                self.player2.r = xcoord2
                self.player2.c = ycoord2

    def getHighScore(self):
        self.names = []
        self.scores = []
        self.highScoreNames = []
        self.highScoreScores = []

        self.highScoreRead = open('HighScore.txt', 'r')
        for line in self.highScoreRead:
            line = line.strip().split(',')
            self.names.append(line[0])
            self.scores.append(int(line[1]))
        self.highScoreRead.close()

        for i in range(10):
            maxval = max(self.scores)
            index = self.scores.index(maxval)
            element = self.scores.pop(index)
            elementName = self.names.pop(index)
            self.highScoreNames.append(elementName)
            self.highScoreScores.append(element)

        # print(self.highScoreNames, self.highScoreScores)


#_____________________________________________________________
screenWidth = 1200
screenHeight = 700
cellWidth = 50
xcoord1 = 6
xcoord2 = 6
ycoord1 = 11
ycoord2 = 13
level = 1

game = Game()

def setup():
    size(screenWidth, screenHeight)
    background(0)
    # frameRate(9)

def draw():

    # background(0)
    if game.state == 'menu':
        background(0)
        fill(230, 0, 38)
        textSize(50)
        fill(0)

        image(game.imgMenu, 0, 0, screenWidth, screenHeight)

        if screenWidth / 2 - 60 < mouseX < screenWidth / 2 - 60 + 120 and screenHeight / 3 - 90 - 50 < mouseY < screenHeight / 3 - 90:
            fill(230, 0, 38)
        else:
            fill(0)

        textSize(60)
        text('Play', screenWidth / 2 - 50, screenHeight / 3 - 90)
        stroke(230, 0, 38)

        if screenWidth / 2 - 70 < mouseX < screenWidth / 2 - 70 + 160 and screenHeight / 3 - 40 < mouseY < screenHeight / 3 - 40 + 35:
            fill(230, 0, 38)
        else:
            fill(0)

        textSize(30)
        text('High Score', screenWidth / 2 - 70, screenHeight / 3 - 10)

     
        # rect(screenWidth/2-60, screenHeight/3-90-50, 120, 55 )
        # rect(screenWidth/2-70, screenHeight/3-40, 160, 35 )

    elif game.state == 'keyControls':
        image(game.imgKeyControls, 0, 0, screenWidth, screenHeight)
        textSize(40)
        fill(255)
        text('Game Controls:', screenWidth / 2 - 140, 100)
        fill(0)
        text('Press Enter to continue...', 380, 675)

    elif game.state == 'play':
        game.display()

    elif game.state == 'highScore':
        game.getHighScore()
        background(7, 6, 57)
        textSize(70)
        fill(255)
        text('High Scores', screenWidth / 2 - 200, 100)
        textSize(25)
        for i in range(10):
            text(game.highScoreNames[i] + ':', 265, 220 + i * 35)
            text(game.highScoreScores[i], 735, 220 + i * 35)
        textSize(15)
        text('Press Enter to return to the main menu...', 450, 152)

    elif game.state == 'score':
        stroke(0)
        image(game.imgScore, 0, 0, screenWidth, screenHeight)
        textSize(50)
        fill(255)
        text(game.winindent + " won!", screenWidth / 2 - 185, 80)
        image(game.player1.imgv, 150, 250, cellWidth, cellWidth, 0, 50, 50, 0)
        image(game.player2.imgv, 650, 250, cellWidth, cellWidth, 0, 50, 50, 0)
        text('Player1: ' + str(game.player1.score), 200, 300)
        text('Player2: ' + str(game.player2.score), 700, 300)
        textSize(40)
        text('Input your name in the boxes below and press Enter:', 100, 400)
        stroke(255)
        if game.input1 == True:
            fill(7, 6, 57)
        else:
            noFill()
        rect(205, 450, 300, 50)

        if game.txt1 != '':
            fill(230, 0, 38)
            text(game.txt1, 215, 485)
            fill(7, 6, 57)

        if game.input2 == True:
            fill(7, 6, 57)
        else:
            noFill()
        rect(705, 450, 300, 50)

        if game.txt2 != '':
            fill(230, 0, 38)
            text(game.txt2, 715, 485)
            fill(7, 6, 57)

        if 400 < mouseX < 950 and 560 < mouseY < 550 + 45:
            fill(230, 0, 38)
        else:
            fill(255)
        text("Click here to return to menu...", 320, 600)


def mousePressed():
    global xcoord1, ycoord1, xcoord2, ycoord2
    if game.state == 'menu':
        if screenWidth / 2 - 60 < mouseX < screenWidth / 2 - 60 + 120 and screenHeight / 3 - 90 - 50 < mouseY < screenHeight / 3 - 90:
            game.state = 'keyControls'
            # game.music.play()
            # game.loadStage()

    if game.state == 'menu':
        if screenWidth / 2 - 70 < mouseX < screenWidth / 2 - 70 + 160 and screenHeight / 3 - 40 < mouseY < screenHeight / 3 - 40 + 35:
            game.state = 'highScore'

    if game.state == 'score' and game.input2 == False and game.clicked1 == 0:
        if 200 < mouseX < 400 and 450 < mouseY < 500:
            game.input1 = True
            game.clicked1 += 1

    if game.state == 'score' and game.input1 == False and game.clicked2 == 0:
        if 700 < mouseX < 900 and 450 < mouseY < 500:
            game.input2 = True
            game.clicked2 += 1

    if game.state == 'score' and game.input1 == False and game.input2 == False:
        if 400 < mouseX < 950 and 560 < mouseY < 550 + 45:
            xcoord1 = 6
            xcoord2 = 6
            ycoord1 = 11
            ycoord2 = 13
            game.__init__()
            game.state = 'menu'
            
            
            


def keyPressed():
    if game.state == 'score' and game.input1 == True:
        if type(key) != int and key.isalpha() or key == ' ':
            game.txt1 += key
        elif keyCode == 8:
            game.txt1 = game.txt1[:len(game.txt1) - 1]

    if game.state == 'score' and game.input2 == True:
        if type(key) != int and key.isalpha() or key == ' ':
            game.txt2 += key
        elif keyCode == 8:
            game.txt2 = game.txt2[:len(game.txt2) - 1]

    if keyCode == UP:
        if game.player1.keyInput[LEFT] == False and game.player1.keyInput[RIGHT] == False and game.player1.keyInput[DOWN] == False:
            game.player1.keyInput[UP] = True
    elif keyCode == DOWN:
        if game.player1.keyInput[LEFT] == False and game.player1.keyInput[RIGHT] == False and game.player1.keyInput[UP] == False:
            game.player1.keyInput[DOWN] = True
    if keyCode == LEFT:
        if game.player1.keyInput[UP] == False and game.player1.keyInput[RIGHT] == False and game.player1.keyInput[DOWN] == False:
            game.player1.keyInput[LEFT] = True
    elif keyCode == RIGHT:
        if game.player1.keyInput[LEFT] == False and game.player1.keyInput[UP] == False and game.player1.keyInput[DOWN] == False:
            game.player1.keyInput[RIGHT] = True

        # player2
        #_____________________________________________________________

    if key == 'w':
        if game.player2.keyInput['A'] == False and game.player2.keyInput['S'] == False and game.player2.keyInput['D'] == False:
            game.player2.keyInput['W'] = True
    elif key == 's':
        if game.player2.keyInput['A'] == False and game.player2.keyInput['W'] == False and game.player2.keyInput['D'] == False:
            game.player2.keyInput['S'] = True
    if key == 'a':
        if game.player2.keyInput['W'] == False and game.player2.keyInput['S'] == False and game.player2.keyInput['D'] == False:
            game.player2.keyInput['A'] = True
    elif key == 'd':
        if game.player2.keyInput['A'] == False and game.player2.keyInput['S'] == False and game.player2.keyInput['W'] == False:
            game.player2.keyInput['D'] = True

    if game.state == 'keyControls' and key == ENTER:
        game.state = 'play'

    if game.state == 'score' and key == ENTER and game.input1 == True:
        game.input1 = False
        highScore = open('HighScore.txt', 'a')
        highScore.write(game.txt1 + ',' + str(game.player1.score) + '\n')
        highScore.close()
        game.txt1 = ''

    if game.state == 'score' and key == ENTER and game.input2 == True:
        game.input2 = False
        highScore = open('HighScore.txt', 'a')
        highScore.write(game.txt2 + ',' + str(game.player2.score) + '\n')
        highScore.close()
        game.txt2 = ''

    if game.state == 'highScore' and key == ENTER:
        game.state = 'menu'


def keyReleased():
    if keyCode == UP:
        game.player1.keyInput[UP] = False
    elif keyCode == DOWN:
        game.player1.keyInput[DOWN] = False
    if keyCode == LEFT:
        game.player1.keyInput[LEFT] = False
    elif keyCode == RIGHT:
        game.player1.keyInput[RIGHT] = False

        #__________________ player2_____________

    if key == 'w':
        game.player2.keyInput['W'] = False
    elif key == 's':
        game.player2.keyInput['S'] = False
    if key == 'a':
        game.player2.keyInput['A'] = False
    elif key == 'd':
        game.player2.keyInput['D'] = False