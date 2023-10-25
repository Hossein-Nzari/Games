import  sys, pygame
from pygame.locals import *

FPS = 10 # frames per second
WINDOWWIDTH = 1920 # width of the window
WINDOWHEIGHT = 1080 # height of the window
SPACESIZE = 145 # radius of each space on the board
BOARDWIDTH = 7 # columns
BOARDHEIGHT = 6 # rows
RED_TILE = 'RED_TILE'
YELLOW_TILE = 'YELLOW_TILE'
EMPTY_SPACE = 'EMPTY_SPACE'
EMPTY_NUM = BOARDWIDTH*BOARDHEIGHT # number of empty spaces at beginning
GRAVITY = {'0': 5, '1': 5, '2': 5, '3': 5, '4': 5, '5': 5, '6': 5} # dict to make the gravity work
YELLOW_LIST = [] # a list for yellow circles' coordinates
RED_LIST = [] # a list for red circles' coordinates

XWASTED = int((WINDOWWIDTH - (BOARDWIDTH * SPACESIZE)) / 2) # wasted area
YWASTED = int((WINDOWHEIGHT - (BOARDHEIGHT * SPACESIZE)) / 2) # wasted area

RED    = (255,  0,  0)
YELLOW = (255,255,  0)
WHITE  = (255,255,255)
BLUE   = (  0,  0,255)
BLACK  = (  0,  0,  0)
ORANGE = (255,165,  0)

TEXTCOLOR = BLACK
TEXTBACKGROUNDCOLOR = ORANGE

def main():
    global MAINCLOCK, DISPLAYSURF, FONT, FONT1, BACKGROUNDIMAGE
    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Connect Four')
    FONT = pygame.font.SysFont('arial.ttf',30)
    FONT1 = pygame.font.SysFont('arial.ttf', 40)

    # Set up the background image. smoothscale fits the images
    boardImage = pygame.image.load('connect4board.png')
    boardImage = pygame.transform.smoothscale(boardImage, (BOARDWIDTH * SPACESIZE, BOARDHEIGHT * SPACESIZE))
    boardImageRect = boardImage.get_rect()
    boardImageRect.topleft = (XWASTED, YWASTED)
    BACKGROUNDIMAGE = pygame.image.load('connect4bg.png')
    BACKGROUNDIMAGE = pygame.transform.smoothscale(BACKGROUNDIMAGE, (WINDOWWIDTH, WINDOWHEIGHT))
    BACKGROUNDIMAGE.blit(boardImage, boardImageRect)

    # Run the main game.
    playGame()

def playGame():
    # Plays connect4 each time this function is called.
    global EMPTY_NUM
    mainBoard = newBoard()
    turn = 'player1'

    # Draw the starting board and ask the player what color they want.
    drawBoard(mainBoard)
    player1Tile, player2Tile = chooseColor()

    while EMPTY_NUM != 0: # main game loop
        # Keep looping for players' turns.

        if turn == 'player1':
            movexy = None
            while movexy == None:
                boardToDraw = mainBoard

                quit()
                for event in pygame.event.get(): # check event's type
                    if event.type == MOUSEBUTTONUP:
                        mousex, mousey = event.pos
                        # movexy is set to a two-item tuple XY coordinate, or None value
                        movexy = getSpaceClicked(mousex, mousey)

                drawBoard(boardToDraw)
                printInfo(turn)

                MAINCLOCK.tick(FPS)
                pygame.display.update()

            # Make the move and end the turn.
            if mainBoard[movexy[0]][movexy[1]] == EMPTY_SPACE:
                Move(mainBoard, player1Tile, movexy[0])
                EMPTY_NUM -= 1
                if finishingMove(player1Tile) == True:
                    break
                turn = 'player2'
            else:
                continue

        else:
            if turn == 'player2':
                movexy = None
                while movexy == None:
                    boardToDraw = mainBoard

                    quit()
                    for event in pygame.event.get():  # check event's type
                        if event.type == MOUSEBUTTONUP:
                            mousex, mousey = event.pos
                            # movexy is set to a two-item tuple XY coordinate, or None value
                            movexy = getSpaceClicked(mousex, mousey)

                    # Draw the game board.
                    drawBoard(boardToDraw)
                    printInfo(turn)

                    MAINCLOCK.tick(FPS)
                    pygame.display.update()

                # Make the move and end the turn.
                if mainBoard[movexy[0]][movexy[1]] == EMPTY_SPACE:
                    Move(mainBoard, player2Tile, movexy[0])
                    EMPTY_NUM -= 1
                    if finishingMove(player2Tile) == True:
                        break
                    turn = 'player1'
                else:
                    continue
    # Display the final score.
    drawBoard(mainBoard)

    # final message

    while not quit():
        if finishingMove(player1Tile) or finishingMove(player2Tile):
            if turn == 'player1':
                text = 'player 1 wins!'
            else :
                text = 'player 2 wins!'
        else:
            text = 'The game is a tie!'

        textSurf = FONT1.render(text, True, TEXTCOLOR, TEXTBACKGROUNDCOLOR)
        textRect = textSurf.get_rect()
        textRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
        DISPLAYSURF.blit(textSurf, textRect)
        quitText = 'Press ESC to quit'

        quitTextSurf = FONT.render(quitText, True, BLACK, WHITE)
        quitTextRect = quitTextSurf.get_rect()
        quitTextRect.center = (XWASTED * 3  / 4, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(quitTextSurf, quitTextRect)

        pygame.display.update()
        MAINCLOCK.tick(FPS)

def boardToPixel(x, y):
    return XWASTED + x * SPACESIZE + int(SPACESIZE / 2), YWASTED + y * SPACESIZE + int(SPACESIZE / 2)


def drawBoard(board):
    # Draw background of board.
    DISPLAYSURF.blit(BACKGROUNDIMAGE, BACKGROUNDIMAGE.get_rect())

    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            # Draw the circles.
            centerx, centery = boardToPixel(x, y)
            pygame.draw.circle(DISPLAYSURF, WHITE, (centerx,centery), 50)

    # Draw the red & yellow circles.
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            centerx, centery = boardToPixel(x, y)
            if board[x][y] == RED_TILE or board[x][y] == YELLOW_TILE:
                if board[x][y] == RED_TILE:
                    tileColor = RED
                else:
                    tileColor = YELLOW
                pygame.draw.circle(DISPLAYSURF, tileColor, (centerx, centery), 50)

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
    turnRect.topleft = (XWASTED / 2 + 25, WINDOWHEIGHT / 2)
    DISPLAYSURF.blit(turnSurf, turnRect)

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

def Move(board, tile,xstart):
    # Place the tile on the board at xstart, ystart, and
    ystart = GRAVITY[str(xstart)]
    board[xstart][ystart] = tile
    GRAVITY[str(xstart)] -= 1

    if tile == YELLOW_TILE:
        YELLOW_LIST.append([xstart,ystart])
    elif tile == RED_TILE:
        RED_LIST.append([xstart,ystart])

def finishingMove(tile):
    i=0
    j=0
    verticalCheck = {'0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[]}
    horizontalCheck = {'0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[]}

    if tile == RED_TILE:
        tileList = RED_LIST
    elif tile == YELLOW_TILE:
        tileList = YELLOW_LIST

    while i<=6:
        for x in tileList:
            if x[0] == i:
                verticalCheck[str(x[0])].append(x[1])
        for value in verticalCheck.values():
            value.sort()
            if {0, 1, 2, 3} <= set(value) or {1, 2, 3, 4} <= set(value) or {2, 3, 4, 5} <= set(value):
                return True
        i += 1

    while j<=7:
        for x in tileList:
            if x[1] == j:
                horizontalCheck[str(x[1])].append(x[0])
        for value in horizontalCheck.values():
            value.sort()
            if {0, 1, 2, 3} <= set(value) or {1, 2, 3, 4} <= set(value) or {2, 3, 4, 5} <= set(value) or {3, 4, 5, 6} <= set(value):
                return True
        j += 1

    for x in tileList:
        k = 1
        while True:
            if [x[0]+k, x[1]+k] in tileList:
                k += 1
                if k == 4:
                    return True
            else:
                break

    for x in tileList:
        l = 1
        while True:
            if [x[0]+l, x[1]-l] in tileList:
                l += 1
                if l == 4:
                    return True
            else:
                break

def newBoard():
    # Creates a new board
    board = []
    for i in range(BOARDWIDTH):
        board.append([EMPTY_SPACE] * BOARDHEIGHT)

    return board

def quit():
    for event in pygame.event.get((QUIT, KEYUP)):
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

if __name__=='__main__':
    main()