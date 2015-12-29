#! /usr/bin/python

# python imports
from math import *
import pygame
from pygame.locals import *

# project imports
from piece import Piece


class GUI:
    def __init__ (self):
        self.display_name = 'Chess AI'
        self.vertical_offset = 50
        self.font = None
        self.screen  = None


    def init(self, monitor_width, monitor_height):
        self.monitor_width  = monitor_width
        self.monitor_height = monitor_height
        self.piece_len = self.monitor_width // 8

        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        self.screen = pygame.display.set_mode((self.monitor_width, self.monitor_height + 2 * self.vertical_offset))
        pygame.display.set_caption(self.display_name)

        #loading images:
        pics = {}
        pics['white'] = [pygame.image.load('resources/WhiteKing.png'), 
                         pygame.image.load('resources/WhiteQueen.png'), 
                         pygame.image.load('resources/WhiteRook.png'), 
                         pygame.image.load('resources/WhiteBishop.png'), 
                         pygame.image.load('resources/WhiteKnight.png'), 
                         pygame.image.load('resources/WhitePawn.png')]

        pics['black'] = [pygame.image.load('resources/BlackKing.png'), 
                         pygame.image.load('resources/BlackQueen.png'), 
                         pygame.image.load('resources/BlackRook.png'), 
                         pygame.image.load('resources/BlackBishop.png'), 
                         pygame.image.load('resources/BlackKnight.png'), 
                         pygame.image.load('resources/BlackPawn.png')]

        for key in pics:
            for i in range(len(pics[key])):
                pics[key][i] = pics[key][i].convert_alpha()
                pics[key][i] = pygame.transform.scale(pics[key][i], (self.piece_len, self.piece_len))

        self.pics = pics


    def translate(self, row, col):
        x = col * self.piece_len
        y = row * self.piece_len + self.vertical_offset
        return x, y



    def reset_screen(self):
        self.screen.fill((20, 20, 20))
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    color = (50, 50, 50)
                else:
                    color = (200, 200, 200)
                x, y = self.translate(row, col)
                pygame.draw.rect(self.screen, color, (x, y, self.piece_len, self.piece_len))


    def draw_piece(self, pic, row, col):
        self.screen.blit(pic, self.translate(row, col))


    def display_team_names(self, name, top):
        text_width, text_height = self.font.size(name)
        if top < 0:
            top += self.monitor_height + 2 * self.vertical_offset - text_height
        self.screen.blit(self.font.render(name, 1, (255, 255, 255)), ((self.screen.get_width() // 2) - text_width / 2, top))


    def show(self, wm):
        self.reset_screen()

        for row in range(len(wm.board)):
            for col in range(len(wm.board[row])):
                part = wm.board[row][col]
                if part.piece != Piece.none:
                    color = 'white' if part.is_white else 'black'
                    piece_num = part.piece.value - 1
                    self.draw_piece(self.pics[color][piece_num], row, col)

        self.display_team_names(wm.black_team_name, 10)
        self.display_team_names(wm.white_team_name, -10)

        #pygame.display.flip()
        pygame.display.update()

