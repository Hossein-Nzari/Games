import  sys, pygame, copy
from pygame.locals import *

FPS = 10 # frames per second
WINDOWWIDTH = 1920 # width of the window
WINDOWHEIGHT = 1080 # height of the window
SPACESIZE = 96 # radius of each space on the board
BOARDWIDTH = 9 # columns
BOARDHEIGHT = 9 # rows
RED_TILE = 'RED_TILE'
YELLOW_TILE = 'YELLOW_TILE'
HINT_TILE = 'HINT_TILE'
EMPTY_SPACE = 'EMPTY_SPACE'
EMPTY_NUM = BOARDWIDTH*BOARDHEIGHT # number of empty spaces at beginning
finalList = [] # a list with coordinates of walls
pressedList = []
hBannedList , vBannedList = [] , []
number = 0 # number to check if a new wall is on board
player1Wall = 10
player2Wall = 10
XWASTED = int((WINDOWWIDTH - (BOARDWIDTH * SPACESIZE)) / 2) # wasted area
YWASTED = int((WINDOWHEIGHT - (BOARDHEIGHT * SPACESIZE)) / 2) # wasted area

RED    = (255,  0,  0)
YELLOW = (255,255,  0)
WHITE  = (255,255,255)
BLUE   = (  0,  0,255)
BLACK  = (  0,  0,  0)
ORANGE = (255,165,  0)
GREEN  = (  0,155,  0)

TEXTCOLOR = BLACK
TEXTBACKGROUNDCOLOR = ORANGE
GRIDLINECOLOR = BLACK
HINTCOLOR = GREEN


def main():
    global MAINCLOCK, DISPLAYSURF, FONT, FONT1, BACKGROUNDIMAGE
    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Connect Four')
    FONT = pygame.font.SysFont('arial.ttf',30)
    FONT1 = pygame.font.SysFont('arial.ttf', 40)

    # Set up the background image. smoothscale fits the images
    boardImage = pygame.image.load('quoridor board.png')
    boardImage = pygame.transform.smoothscale(boardImage, (BOARDWIDTH * SPACESIZE, BOARDHEIGHT * SPACESIZE))
    boardImageRect = boardImage.get_rect()
    boardImageRect.topleft = (XWASTED, YWASTED)
    BACKGROUNDIMAGE = pygame.image.load('bg.png')
    BACKGROUNDIMAGE = pygame.transform.smoothscale(BACKGROUNDIMAGE, (WINDOWWIDTH, WINDOWHEIGHT))
    BACKGROUNDIMAGE.blit(boardImage, boardImageRect)

    # Run the main game.
    playGame()

def playGame():
    global validRed,validYellow
    # Plays Quoridor each time this function is called.
    mainBoard = newBoard()

    hintsSurf = FONT.render('Hints', True, TEXTCOLOR, TEXTBACKGROUNDCOLOR)
    hintsRect = hintsSurf.get_rect()
    hintsRect.center = (WINDOWWIDTH - XWASTED / 2 - 100 , WINDOWHEIGHT / 2)

    wallsSurf = FONT.render('Walls', True, TEXTCOLOR, TEXTBACKGROUNDCOLOR)
    wallsRect = wallsSurf.get_rect()
    wallsRect.topleft = (XWASTED / 2 + 25, WINDOWHEIGHT / 2)

    turn = 'player1'

    # Draw the starting board and ask the player what color they want.
    drawBoard(mainBoard)
    player1Tile, player2Tile = chooseColor()

    while True:  # main game loop
        # Keep looping for players' turns.

        showHints = False
        clickWall = False
        turnChanger = 0
        copyNumber = number
        validMoves(mainBoard, player1Tile)
        validMoves(mainBoard, player2Tile)
        if player1Tile == RED_TILE:
            a = validRed
            b = validYellow
        else:
            a = validYellow
            b = validRed

        if turn == 'player1':
            movexy = None
            while movexy == None and turnChanger == 0:
                if showHints:
                    boardToDraw = boardsValidMoves(mainBoard, player1Tile)
                else:
                    boardToDraw = mainBoard

                quit()
                for event in pygame.event.get():  # check event's type
                    if event.type == MOUSEBUTTONUP:
                        mousex, mousey = event.pos
                        if hintsRect.collidepoint( (mousex, mousey) ):
                            showHints = not showHints

                        if wallsRect.collidepoint( (mousex, mousey) ):
                            clickWall = not clickWall
                            if clickWall == True and player1Wall > 0:
                                getWall('player1')
                            if number - copyNumber == 1:
                                turnChanger = 1
                                turn = 'player2'

                        # movexy is set to a two-item tuple XY coordinate, or None value
                        else:
                            movexy = getSpaceClicked(mousex, mousey)

                drawBoard(boardToDraw)
                printInfo(turn)

                DISPLAYSURF.blit(hintsSurf, hintsRect)
                DISPLAYSURF.blit(wallsSurf, wallsRect)

                MAINCLOCK.tick(FPS)
                pygame.display.update()

            # Make the move and end the turn.

            if turnChanger == 1:
                continue

            elif list(movexy) in a:
                Move(mainBoard, player1Tile, movexy[0], movexy[1])
                if finishingMove(mainBoard, player1Tile) == True:
                    break
                turn = 'player2'

        elif turn == 'player2':
            movexy = None
            while movexy == None and turnChanger == 0:
                if showHints:
                    boardToDraw = boardsValidMoves(mainBoard, player2Tile)
                else:
                    boardToDraw = mainBoard

                quit()
                for event in pygame.event.get():  # check event's type
                    if event.type == MOUSEBUTTONUP:
                        mousex, mousey = event.pos
                        if hintsRect.collidepoint((mousex, mousey)):
                            showHints = not showHints

                        if wallsRect.collidepoint((mousex, mousey)):
                            clickWall = not clickWall
                            if clickWall == True and player2Wall > 0:
                                getWall('player2')
                            if number - copyNumber == 1:
                                turnChanger = 1
                                turn = 'player1'

                        # movexy is set to a two-item tuple XY coordinate, or None value
                        movexy = getSpaceClicked(mousex, mousey)

                # Draw the game board.
                drawBoard(boardToDraw)
                printInfo(turn)

                DISPLAYSURF.blit(hintsSurf, hintsRect)
                DISPLAYSURF.blit(wallsSurf, wallsRect)

                MAINCLOCK.tick(FPS)
                pygame.display.update()

            # Make the move and end the turn.
            if turnChanger == 1:
                continue
            elif list(movexy) in b:
                Move(mainBoard, player2Tile, movexy[0], movexy[1])
                if finishingMove(mainBoard, player2Tile) == True:
                    break
                turn = 'player1'


    # Display the final score.
    drawBoard(mainBoard)

    # final message

    while not quit():
        if finishingMove(mainBoard, player1Tile) or finishingMove(mainBoard, player2Tile):
            if turn == 'player1':
                text = 'player 1 wins!'
            else:
                text = 'player 2 wins!'

        textSurf = FONT1.render(text, True, TEXTCOLOR, TEXTBACKGROUNDCOLOR)
        textRect = textSurf.get_rect()
        textRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
        DISPLAYSURF.blit(textSurf, textRect)
        quitText = 'Press ESC to quit'

        quitTextSurf = FONT.render(quitText, True, BLACK, WHITE)
        quitTextRect = quitTextSurf.get_rect()
        quitTextRect.center = (XWASTED * 3 / 4, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(quitTextSurf, quitTextRect)

        pygame.display.update()
        MAINCLOCK.tick(FPS)

def boardToPixel(x, y):
    return XWASTED + x * SPACESIZE + int(SPACESIZE / 2), YWASTED + y * SPACESIZE + int(SPACESIZE / 2)

def getWall(turn):
    global finalList, number, player1Wall, player2Wall,pressedList,hBannedList,vBannedList


    wallInfoSurf = FONT.render("enter H or V and 2 numbers (or M)", True, TEXTCOLOR)
    wallInfoRect = wallInfoSurf.get_rect()
    wallInfoRect.topleft = (XWASTED / 2 - 67, WINDOWHEIGHT / 2 + 390)
    DISPLAYSURF.blit(wallInfoSurf, wallInfoRect)
    MAINCLOCK.tick(FPS)
    pygame.display.update()

    coordList = []
    HoV = ''

    while (len(coordList) != 2 and HoV != 'h') or (len(coordList) != 2 and HoV != 'v'):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                    return False

                if event.key == pygame.K_1:
                    coordList.append(1)

                if event.key == pygame.K_2:
                    coordList.append(2)

                if event.key == pygame.K_3:
                    coordList.append(3)

                if event.key == pygame.K_4:
                    coordList.append(4)

                if event.key == pygame.K_5:
                    coordList.append(5)

                if event.key == pygame.K_6:
                    coordList.append(6)

                if event.key == pygame.K_7:
                    coordList.append(7)

                if event.key == pygame.K_8:
                    coordList.append(8)

                if event.key == pygame.K_v:
                    HoV = 'v'

                if event.key == pygame.K_h:
                    HoV = 'h'

    if [HoV, coordList] in finalList:
        return False


    for i in pressedList:
        if HoV == 'h' and i[0] == 'v' and coordList == i[1]:
            return False
        elif HoV == 'v' and i[0] == 'h' and coordList == i[1]:
            return False
        if HoV == 'h' and i[0] == 'h' and [coordList[0], coordList[1] + 1] == i[1]:
            return False
        elif HoV == 'v' and i[0] == 'v' and [coordList[0] + 1, coordList[1]] == i[1]:
            return False

    pressedList.append([HoV, coordList])
    finalList.append([HoV, coordList])
    if HoV == 'v':
        finalList.append([HoV, [coordList[0] + 1, coordList[1]]])
    elif HoV =='h':
        finalList.append([HoV, [coordList[0], coordList[1] + 1]])
    number += 1
    for i in finalList:
        if i[0] == 'h':
            hBannedList.append([[i[1][1]-1, i[1][0]-1], [i[1][1]-1, i[1][0]]])
        elif i[0] == 'v':
            vBannedList.append([[i[1][1]-1, i[1][0]-1], [i[1][1], i[1][0]-1]])
    if turn == 'player1':
        player1Wall -= 1
    elif turn == 'player2':
        player2Wall -= 1
    return True


def drawBoard(board):
    # Draw background of board.
    DISPLAYSURF.blit(BACKGROUNDIMAGE, BACKGROUNDIMAGE.get_rect())

    # Draw grid lines of the board.
    for x in range(BOARDWIDTH + 1):
        # Draw the horizontal lines.
        startx = (x * SPACESIZE) + XWASTED
        starty = YWASTED
        endx = (x * SPACESIZE) + XWASTED
        endy = YWASTED + (BOARDHEIGHT * SPACESIZE)
        pygame.draw.line(DISPLAYSURF, GRIDLINECOLOR, (startx, starty), (endx, endy))
    for y in range(BOARDHEIGHT + 1):
        # Draw the vertical lines.
        startx = XWASTED
        starty = (y * SPACESIZE) + YWASTED
        endx = XWASTED + (BOARDWIDTH * SPACESIZE)
        endy = (y * SPACESIZE) + YWASTED
        pygame.draw.line(DISPLAYSURF, GRIDLINECOLOR, (startx, starty), (endx, endy))

    if len(finalList) > 0:
        i = 0
        while i in range(len(finalList)):
            if finalList[i][0] == 'h':
                startx = ((finalList[i][1][1] - 1) * SPACESIZE) + XWASTED
                starty = ((finalList[i][1][0]) * SPACESIZE) + YWASTED
                endx = ((finalList[i][1][1]) * SPACESIZE) + XWASTED
                endy = ((finalList[i][1][0]) * SPACESIZE) + YWASTED
                pygame.draw.line(DISPLAYSURF, BLUE, (startx, starty), (endx, endy))
                i += 1

            elif finalList[i][0] == 'v':
                startx = ((finalList[i][1][1]) * SPACESIZE) + XWASTED
                starty = ((finalList[i][1][0] - 1) * SPACESIZE) + YWASTED
                endx = ((finalList[i][1][1]) * SPACESIZE) + XWASTED
                endy = ((finalList[i][1][0]) * SPACESIZE) + YWASTED
                pygame.draw.line(DISPLAYSURF, BLUE, (startx, starty), (endx, endy))
                i += 1

    # Draw the red and yellow tiles or hint spots.
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            centerx, centery = boardToPixel(x, y)
            if board[x][y] == RED_TILE or board[x][y] == YELLOW_TILE:
                if board[x][y] == RED_TILE:
                    tileColor = RED
                else:
                    tileColor = YELLOW
                pygame.draw.circle(DISPLAYSURF, tileColor, (centerx, centery), int(SPACESIZE / 2) - 4)
            if board[x][y] == HINT_TILE:
                pygame.draw.rect(DISPLAYSURF, HINTCOLOR, (centerx - 4, centery - 4, 8, 8))

def getSpaceClicked(mousex, mousey):
    # Return a tuple of two integers of the board space coordinates where
    # the mouse was clicked. Or returns None
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if mousex > x * SPACESIZE + XWASTED and \
               mousex < (x + 1) * SPACESIZE + XWASTED and \
               mousey > y * SPACESIZE + YWASTED and \
               mousey < (y + 1) * SPACESIZE + YWASTED:
                return (x, y)
    return None


def printInfo(turn):
    # Draws scores and whose turn it is on the screen.
    turnSurf = FONT.render("%s's Turn" % (turn.title()), True, TEXTCOLOR)
    turnRect = turnSurf.get_rect()
    turnRect.topleft = (XWASTED / 2 + 25, WINDOWHEIGHT / 2 + 60)
    DISPLAYSURF.blit(turnSurf, turnRect)

    p1wallSurf = FONT.render("P1 Wall:%s" % (player1Wall), True, TEXTCOLOR)
    p1wallRect = p1wallSurf.get_rect()
    p1wallRect.topleft = (XWASTED / 2 + 25, WINDOWHEIGHT / 2 + 90)
    DISPLAYSURF.blit(p1wallSurf, p1wallRect)

    p2wallSurf = FONT.render("P2 Wall:%s" % (player2Wall), True, TEXTCOLOR)
    p2wallRect = p2wallSurf.get_rect()
    p2wallRect.topleft = (XWASTED / 2 + 25, WINDOWHEIGHT / 2 + 120)
    DISPLAYSURF.blit(p2wallSurf, p2wallRect)

def isOnBoard(x, y):
    # Returns True if the coordinates are located on the board.
    return x >= 0 and x < BOARDWIDTH and y >= 0 and y < BOARDHEIGHT

def chooseColor():
    # Draws the text and handles the mouse click events for letting
    # the player choose which color they want to be.  Returns
    # [RED_TILE, YELLOW_TILE] if the player chooses to be RED,
    # [YELLOW_TILE, RED_TILE] if YELLOW.

    # Create the text.
    textSurf = FONT.render('Do you want to be RED or YELLOW?', True,TEXTCOLOR, TEXTBACKGROUNDCOLOR)
    textRect = textSurf.get_rect()
    textRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))

    xSurf = FONT1.render('RED', True, TEXTCOLOR, TEXTBACKGROUNDCOLOR)
    xRect = xSurf.get_rect()
    xRect.center = (int(WINDOWWIDTH / 2) - 72, int(WINDOWHEIGHT / 2) + 40)

    oSurf = FONT1.render('YELLOW', True, TEXTCOLOR, TEXTBACKGROUNDCOLOR)
    oRect = oSurf.get_rect()
    oRect.center = (int(WINDOWWIDTH / 2) + 50, int(WINDOWHEIGHT / 2) + 40)

    while True:
        quit()
        for event in pygame.event.get(): # check event's type
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if xRect.collidepoint( (mousex, mousey) ):
                    return [RED_TILE, YELLOW_TILE]
                elif oRect.collidepoint( (mousex, mousey) ):
                    return [YELLOW_TILE, RED_TILE]

        # Draw the screen.
        DISPLAYSURF.blit(textSurf, textRect)
        DISPLAYSURF.blit(xSurf, xRect)
        DISPLAYSURF.blit(oSurf, oRect)
        pygame.display.update()
        MAINCLOCK.tick(FPS)

def Move(board, tile, xstart, ystart):
    availableMoves = validMoves(board,tile)
    if [xstart, ystart] in availableMoves:
        for column in board:
            for row in column:
                if row == tile:
                    board[board.index(column)][column.index(row)] = EMPTY_SPACE
        board[xstart][ystart] = tile
    else:
        return False


def finishingMove(board, tile):

    for column in board:
        for row in column:
            if row == tile:
                indexTile = [board.index(column), column.index(row)]


    firstRow = [[i, 0] for i in range(9)]
    lastRow  = [[i, 8] for i in range(9)]

    if tile == YELLOW_TILE:
        if indexTile in firstRow:
            return True
    elif tile == RED_TILE:
        if indexTile in lastRow:
            return True


def validMoves(board, tile):
    global leastWall, validList,validRed,validYellow,hBannedList,vBannnedList
    DOWN  = [ 0,  1]
    LEFT  = [-1,  0]
    RIGHT = [ 1,  0]
    UP    = [ 0, -1]
    validList = []

    if tile == RED_TILE:
        otherTile = YELLOW_TILE
    else:
        otherTile = RED_TILE

    for column in board:
        for row in column:
            if row == tile:
                indexTile = [board.index(column), column.index(row)]
            elif row == otherTile:
                indexOtherTile = [board.index(column), column.index(row)]


    if [x + y for x, y in zip(indexTile, UP)] != indexOtherTile and [[x + y for x, y in zip(indexTile, UP)], indexTile] not in hBannedList:
        validList.append([x + y for x, y in zip(indexTile, UP)])

    if [x + y for x, y in zip(indexTile, UP)] == indexOtherTile and [[x + y for x, y in zip(indexTile, UP)], indexTile]\
            not in hBannedList and [[x + y for x, y in zip(indexOtherTile, UP)], indexOtherTile] not in hBannedList:
        validList.append([x + y + y for x, y in zip(indexTile, UP)])

    elif [x + y for x, y in zip(indexTile, UP)] == indexOtherTile and [[x + y for x, y in zip(indexTile, UP)], indexTile]\
            not in hBannedList and [[x + y for x, y in zip(indexOtherTile, UP)], indexOtherTile] in hBannedList:
        if [indexOtherTile, [x + y for x, y in zip(indexOtherTile, RIGHT)]] not in vBannedList:
            validList.append([x + y + z for x, y, z in zip(indexTile, UP, RIGHT)])
        if [[x + y for x, y in zip(indexOtherTile, LEFT)], indexOtherTile] not in vBannedList:
            validList.append([x + y + z for x, y, z in zip(indexTile, UP, LEFT)])

    if [x + y for x, y in zip(indexTile, DOWN)] != indexOtherTile and [indexTile, [x + y for x, y in zip(indexTile, DOWN)]] not in hBannedList:
        validList.append([x + y for x, y in zip(indexTile, DOWN)])
    if [x + y for x, y in zip(indexTile, DOWN)] == indexOtherTile and [indexTile, [x + y for x, y in zip(indexTile, DOWN)]]\
            not in hBannedList and [indexOtherTile, [x + y for x, y in zip(indexOtherTile, DOWN)]] not in hBannedList:
        validList.append([x + y + y for x, y in zip(indexTile, DOWN)])
    elif [x + y for x, y in zip(indexTile, DOWN)] == indexOtherTile and [indexTile, [x + y for x, y in zip(indexTile, DOWN)]] not in hBannedList\
            and [indexOtherTile, [x + y for x, y in zip(indexOtherTile, DOWN)]] in hBannedList:
        if [indexOtherTile, [x + y for x, y in zip(indexOtherTile, RIGHT)]] not in vBannedList:
            validList.append([x + y + z for x, y, z in zip(indexTile, DOWN, RIGHT)])
        if [[x + y for x, y in zip(indexOtherTile, LEFT)], indexOtherTile] not in vBannedList:
            validList.append([x + y + z for x, y, z in zip(indexTile, DOWN, LEFT)])

    if [x + y for x, y in zip(indexTile, RIGHT)] != indexOtherTile and [indexTile, [x + y for x, y in zip(indexTile, RIGHT)]] not in vBannedList:
        validList.append([x + y for x, y in zip(indexTile, RIGHT)])
    if [x + y for x, y in zip(indexTile, RIGHT)] == indexOtherTile and [indexTile, [x + y for x, y in zip(indexTile, RIGHT)]]\
            not in vBannedList and [indexOtherTile, [x + y for x, y in zip(indexOtherTile, RIGHT)]] not in vBannedList:
        validList.append([x + y + y for x, y in zip(indexTile, RIGHT)])
    elif [x + y for x, y in zip(indexTile, RIGHT)] == indexOtherTile and [indexTile, [x + y for x, y in zip(indexTile, RIGHT)]] not in vBannedList\
            and [indexOtherTile, [x + y for x, y in zip(indexOtherTile, RIGHT)]] in vBannedList:
        if [[x + y for x, y in zip(indexOtherTile, UP)], indexOtherTile] not in hBannedList:
            validList.append([x + y + z for x, y, z in zip(indexTile, UP, RIGHT)])
        if [indexOtherTile, [x + y for x, y in zip(indexOtherTile, LEFT)]] not in hBannedList:
            validList.append([x + y + z for x, y, z in zip(indexTile, DOWN, RIGHT)])

    if [x + y for x, y in zip(indexTile, LEFT)] != indexOtherTile and [[x + y for x, y in zip(indexTile, LEFT)], indexTile] not in vBannedList:
        validList.append([x + y for x, y in zip(indexTile, LEFT)])
    if [x + y for x, y in zip(indexTile, LEFT)] == indexOtherTile and [[x + y for x, y in zip(indexTile, LEFT)], indexTile]\
            not in vBannedList and [[x + y for x, y in zip(indexOtherTile, LEFT)], indexOtherTile] not in vBannedList:
        validList.append([x + y + y for x, y in zip(indexTile, LEFT)])
    elif [x + y for x, y in zip(indexTile, LEFT)] == indexOtherTile and [[x + y for x, y in zip(indexTile, LEFT)], indexTile]\
            not in vBannedList and [[x + y for x, y in zip(indexOtherTile, LEFT)], indexOtherTile] in vBannedList:
        if [[x + y for x, y in zip(indexOtherTile, UP)], indexOtherTile] not in hBannedList:
            validList.append([x + y + z for x, y, z in zip(indexTile, UP, LEFT)])
        if [indexOtherTile, [x + y for x, y in zip(indexOtherTile, DOWN)]] not in hBannedList:
            validList.append([x + y + z for x, y, z in zip(indexTile, DOWN, LEFT)])


    for x in validList:
        for y in x:
            if y < 0 or y > 8:
                validList.remove(x)
    for x in validList:
        if indexOtherTile in validList:
            validList.remove(indexOtherTile)
    if tile == RED_TILE:
        validRed = validList
    else:
        validYellow = validList
    return validList


def boardsValidMoves(board, tile):
    # Returns a new board with hint markings.
    dupeBoard = copy.deepcopy(board)
    for x, y in validMoves(dupeBoard, tile):
        dupeBoard[x][y] = HINT_TILE
    return dupeBoard



def newBoard():
    # Creates a new board
    board = []
    for i in range(BOARDWIDTH):
        board.append([EMPTY_SPACE] * BOARDHEIGHT)

    board[4][0] = RED_TILE
    board[4][8] = YELLOW_TILE

    return board

def quit():
    for event in pygame.event.get((QUIT, KEYUP)):
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

if __name__=='__main__':
    main()