import pygame
import sys
from pygame.locals import *
import numpy as np
import math

ROW = 6
COLUMN = 7


# initializing colors

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)


# this funciton to create the board of zeros 6 rows and 7 columns

def create_board():
    board = np.zeros((6, 7))
    return board


# this funciton to draw the pieces in the board

def draw_board(board):
    for r in range(ROW):
        for c in range(COLUMN):
            if board[r][c] == 1:
                red_coin = pygame.image.load('red_coin_transparent.png')
                screen.blit(red_coin, ((c*100)+49, 500-(r*100)+100))
            elif board[r][c] == 2:
                yellow_coin = pygame.image.load('yellow_coin_transparent.png')
                screen.blit(yellow_coin, ((c*100)+49, 500-(r*100)+100))
    pygame.display.update()


# this funciton to check if the column has any empty place to

def valid_position(board, column):
    return board[5][column] == 0


def get_next_open_row(board, column):
    for r in range(ROW):
        if board[r][column] == 0:
            return r


def drop_piece(board, row, column, piece):
    board[row][column] = piece


def winner(board, piece):
    for c in range(COLUMN-3):
        for r in range(ROW):
            if r < 3:
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True
            else:
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True
    for c in range(COLUMN):
        for r in range(ROW-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    for c in range(COLUMN-3):
        for r in range(ROW):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True


pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("CONNECT 4")
icon = pygame.image.load('program icon.png').convert_alpha()
pygame.display.set_icon(icon)

background_image = pygame.image.load('background.png').convert_alpha()
red_coin = pygame.image.load('red_coin_transparent.png').convert_alpha()
yellow_coin = pygame.image.load('yellow_coin_transparent.png').convert_alpha()
up_coin = False
board = create_board()
turn = 0
game_over = False
fontObj = pygame.font.Font('freesansbold.ttf', 32)


draw_board(board)
pygame.display.update()

while not game_over:
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if turn % 2 == 0:
                posx = event.pos[0]
                column = int(math.floor((posx-49)/100))

                if valid_position(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 1)
                    if winner(board, 1):
                        label = fontObj.render(
                            "First player is the winner", True, RED)
                        screen.blit(label, (350, 732))
                        game_over = True
                    up_coin = True
                else:
                    turn += 1

            else:
                posx = event.pos[0]
                column = int(math.floor((posx-49)/100))

                if valid_position(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 2)
                    if winner(board, 2):
                        label = fontObj.render(
                            "Second player is the winner", True, YELLOW)
                        screen.blit(label, (320, 732))
                        game_over = True
                    up_coin = False
                else:
                    turn += 1

            turn += 1
        draw_board(board)
        screen.blit(background_image, (0, 0))
        if mx > 49 and mx < 749:
            if not up_coin:
                screen.blit(red_coin, (mx-50, 0))
            else:
                screen.blit(yellow_coin, (mx-50, 0))
        if game_over:
            pygame.time.wait(2000)
