from piece import Piece
from part import Part
from move import Move


class WorldModel:
    def __init__(self):
        self.board = [[Part(piece=Piece.none) for _ in range(8)] for _ in range(8)]
        self.white_team_name = ''
        self.black_team_name = ''
        self.my_color = ''


    def __str__(self):
        res = ''
        for row in self.board:
            for part in row:
                if part.piece != Piece.none:
                    res += ('+' if part.is_white else '-') + part.piece.name + '\t'
                else:
                    res += part.piece.name + '\t'
            res += '\n'
        return res


    def init(self, white_name, black_name, my_color):
        first_row = [Piece.rook, Piece.knight, Piece.bishop, Piece.queen, Piece.king, Piece.bishop, Piece.knight, Piece.rook]
        for i in range(8):
            ### white pieces
            self.board[7][i].is_white = True
            self.board[7][i].piece = first_row[i]
            self.board[6][i].is_white = True
            self.board[6][i].piece = Piece.pawn
            ### black pieces
            self.board[0][i].is_white = False
            self.board[0][i].piece = first_row[i]
            self.board[1][i].is_white = False
            self.board[1][i].piece = Piece.pawn

        self.white_team_name = white_name
        self.black_team_name = black_name
        self.my_color = my_color


    def all_moves(self, is_white):

        def get_not_king_moves (is_white):
            moves = []
            for row_num in range (8):
                for col_num in range (8):
                    part = self.board [row_num][col_num]
                    if part.piece != Piece.none:
                        #white
                        if part.is_white and is_white:
                            #pawn
                            if part.piece == Piece.pawn:
                                if row_num > 0:

                                    if self.board [row_num - 1][col_num].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num-1, col_num)))
                                    if col_num>0:
                                        if self.board [row_num-1][col_num-1].piece != Piece.none and not self.board [row_num-1][col_num-1].is_white:
                                            moves.append (Move((row_num, col_num), (row_num-1, col_num-1)))
                                    if col_num<7:
                                        if self.board [row_num-1][col_num+1].piece != Piece.none and not self.board [row_num-1][col_num+1].is_white:
                                            moves.append (Move((row_num, col_num), (row_num-1, col_num+1)))
                                if row_num == 6:
                                    if self.board [row_num - 2][col_num].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num-2, col_num)))
                            #rook
                            if part.piece == Piece.rook:
                                c = 1
                                while row_num - c >= 0:
                                    if self.board [row_num-c][col_num].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num)))
                                        c = c+1
                                    elif not self.board [row_num-c][col_num].is_white:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num)))
                                        break
                                    else:
                                        break
                                c = 1
                                while row_num + c <= 7: 
                                    if self.board [row_num+c][col_num].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num)))
                                        c = c+1
                                    elif not self.board [row_num+c][col_num].is_white:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num)))
                                        break
                                    else:
                                        break
                                c = 1
                                while col_num - c >= 0:
                                    if self.board [row_num][col_num-c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num, col_num-c)))
                                        c = c+1
                                    elif not self.board [row_num][col_num-c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num, col_num-c)))
                                        break
                                    else:
                                        break
                                c = 1
                                while col_num + c <= 7:
                                    if self.board [row_num][col_num+c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num, col_num+c)))
                                        c = c+1
                                    elif not self.board [row_num][col_num+c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num, col_num+c)))
                                        break
                                    else:
                                        break                                    
                            #bishop
                            if part.piece == Piece.bishop:
                                c = 1
                                while row_num - c >= 0 and col_num - c >= 0:
                                    if self.board [row_num-c][col_num-c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num-c)))
                                        c = c+1
                                    elif not self.board [row_num-c][col_num-c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num-c)))
                                        break
                                    else:
                                        break

                                c = 1
                                while row_num + c <= 7 and col_num + c <= 7:
                                    if self.board [row_num+c][col_num+c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num+c)))
                                        c = c+1
                                    elif not self.board [row_num+c][col_num+c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num+c)))
                                        break
                                    else:
                                        break
                                c = 1
                                while col_num - c >= 0 and row_num + c <= 7:
                                    if self.board [row_num+c][col_num-c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num-c)))
                                        c = c+1
                                    elif not self.board [row_num+c][col_num-c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num-c)))
                                        break
                                    else:
                                        break
                                
                                c = 1
                                while col_num + c <= 7 and row_num - c >= 0:
                                    if self.board [row_num-c][col_num+c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num+c)))
                                        c = c+1
                                    elif not self.board [row_num-c][col_num+c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num+c)))
                                        break
                                    else:
                                        break
                                
                            #knight
                            if part.piece == Piece.knight:
                                if row_num >=2:
                                    if col_num<=6:
                                        if self.board [row_num-2][col_num+1].piece == Piece.none or self.board [row_num-2][col_num+1].piece != Piece.none and not self.board [row_num-2][col_num+1].is_white:
                                            moves.append(Move((row_num, col_num), (row_num-2,col_num+1)))
                                    if col_num>=1:
                                        if self.board [row_num-2][col_num-1].piece == Piece.none or self.board [row_num-2][col_num-1].piece != Piece.none and not self.board [row_num-2][col_num-1].is_white:
                                            moves.append(Move((row_num, col_num), (row_num-2,col_num-1)))
                                if row_num >=1:
                                    if col_num<=5:
                                        if self.board [row_num-1][col_num+2].piece == Piece.none or self.board [row_num-1][col_num+2].piece != Piece.none and not self.board [row_num-1][col_num+2].is_white:
                                            moves.append(Move((row_num, col_num), (row_num-1,col_num+2)))
                                    if col_num>=2:
                                        if self.board [row_num-1][col_num-2].piece == Piece.none or self.board [row_num-1][col_num-2].piece != Piece.none and not self.board [row_num-1][col_num-2].is_white:
                                            moves.append(Move((row_num, col_num), (row_num-1,col_num-2)))
                                if row_num <=5:
                                    if col_num<=6:
                                        if self.board [row_num+2][col_num+1].piece == Piece.none or self.board [row_num+2][col_num+1].piece != Piece.none and not self.board [row_num+2][col_num+1].is_white:    
                                            moves.append(Move((row_num, col_num), (row_num+2,col_num+1)))
                                    if col_num>=1:
                                        if self.board [row_num+2][col_num-1].piece == Piece.none or self.board [row_num+2][col_num-1].piece != Piece.none and not self.board [row_num+2][col_num-1].is_white:
                                            moves.append(Move((row_num, col_num), (row_num+2,col_num-1)))
                                if row_num <=6:
                                    if col_num<=5:
                                        if self.board [row_num+1][col_num+2].piece == Piece.none or self.board [row_num+1][col_num+2].piece != Piece.none and not self.board [row_num+1][col_num+2].is_white:
                                            moves.append(Move((row_num, col_num), (row_num+1,col_num+2)))
                                    if col_num>=2:
                                        if self.board [row_num+1][col_num-2].piece == Piece.none or self.board [row_num+1][col_num-2].piece != Piece.none and not self.board [row_num+1][col_num-2].is_white:
                                            moves.append(Move((row_num, col_num), (row_num+1,col_num-2)))
                            #queen
                            if part.piece == Piece.queen:
                                c = 1
                                while row_num - c >= 0:
                                    if self.board [row_num-c][col_num].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num)))
                                        c = c+1
                                    elif not self.board [row_num-c][col_num].is_white:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num)))
                                        break
                                    else:
                                        break
                                c = 1
                                while row_num + c <= 7: 
                                    if self.board [row_num+c][col_num].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num)))
                                        c = c+1
                                    elif not self.board [row_num+c][col_num].is_white:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num)))
                                        break
                                    else:
                                        break
                                c = 1
                                while col_num - c >= 0:
                                    if self.board [row_num][col_num-c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num, col_num-c)))
                                        c = c+1
                                    elif not self.board [row_num][col_num-c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num, col_num-c)))
                                        break
                                    else:
                                        break
                                c = 1
                                while col_num + c <= 7:
                                    if self.board [row_num][col_num+c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num, col_num+c)))
                                        c = c+1
                                    elif not self.board [row_num][col_num+c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num, col_num+c)))
                                        break
                                    else:
                                        break                                    
                            if part.piece == Piece.bishop:
                                c = 1
                                while row_num - c >= 0 and col_num - c >= 0:
                                    if self.board [row_num-c][col_num-c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num-c)))
                                        c = c+1
                                    elif not self.board [row_num-c][col_num-c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num-c)))
                                        break
                                    else:
                                        break

                                c = 1
                                while row_num + c <= 7 and col_num + c <= 7:
                                    if self.board [row_num+c][col_num+c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num+c)))
                                        c = c+1
                                    elif not self.board [row_num+c][col_num+c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num+c)))
                                        break
                                    else:
                                        break
                                c = 1
                                while col_num - c >= 0 and row_num + c <= 7:
                                    if self.board [row_num+c][col_num-c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num-c)))
                                        c = c+1
                                    elif not self.board [row_num+c][col_num-c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num-c)))
                                        break
                                    else:
                                        break
                                
                                c = 1
                                while col_num + c <= 7 and row_num - c >= 0:
                                    if self.board [row_num-c][col_num+c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num+c)))
                                        c = c+1
                                    elif not self.board [row_num-c][col_num+c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num+c)))
                                        break
                                    else:
                                        break
                                
                        #black
                        if not part.is_white and not is_white:
                            #pawn
                            if part.piece == Piece.pawn:
                                if row_num < 7:
                                    if self.board [row_num + 1][col_num].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num+1, col_num)))
                                    if col_num>0:
                                        if self.board [row_num+1][col_num-1].piece != Piece.none and self.board [row_num+1][col_num-1].is_white:
                                            moves.append (Move((row_num, col_num), (row_num+1, col_num-1)))
                                    if col_num<7:
                                        if self.board [row_num+1][col_num+1].piece != Piece.none and self.board [row_num+1][col_num+1].is_white:
                                            moves.append (Move((row_num, col_num), (row_num+1, col_num+1)))
                                        
                                if row_num == 1:
                                    if self.board [row_num + 2][col_num].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num+2, col_num)))
                            #rook
                            if part.piece == Piece.rook:
                                c = 1
                                while row_num - c >= 0:
                                    if self.board [row_num-c][col_num].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num)))
                                        c = c+1
                                    elif self.board [row_num-c][col_num].is_white:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num)))
                                        break
                                    else:
                                        break
                                c = 1                                
                                while row_num + c <= 7: 
                                    if self.board [row_num+c][col_num].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num)))
                                        c = c+1
                                        
                                    elif self.board [row_num+c][col_num].is_white:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num)))
                                        break
                                    else:
                                        break
                                c = 1
                                while col_num - c >= 0:
                                    if self.board [row_num][col_num-c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num, col_num-c)))
                                        c = c+1
                                    elif self.board [row_num][col_num-c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num, col_num-c)))
                                        break
                                    else:
                                        break
                                c = 1
                                while col_num + c <= 7:
                                    if self.board [row_num][col_num+c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num, col_num+c)))
                                        c = c+1
                                    elif self.board [row_num][col_num+c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num, col_num+c)))
                                        break
                                    else:
                                        break                                    
                            #bishop
                            if part.piece == Piece.bishop:
                                c = 1
                                while row_num - c >= 0 and col_num - c >= 0:
                                    if self.board [row_num-c][col_num-c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num-c)))
                                        c = c+1
                                    elif self.board [row_num-c][col_num-c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num-c)))
                                        break
                                    else:
                                        break

                                c = 1
                                while row_num + c <= 7 and col_num + c <= 7:
                                    if self.board [row_num+c][col_num+c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num+c)))
                                        c = c+1
                                    elif self.board [row_num+c][col_num+c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num+c)))
                                        break
                                    else:
                                        break
                                c = 1
                                while col_num - c >= 0 and row_num + c <= 7:
                                    if self.board [row_num+c][col_num-c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num-c)))
                                        c = c+1
                                    elif self.board [row_num+c][col_num-c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num-c)))
                                        break
                                    else:
                                        break
                                
                                c = 1
                                while col_num + c <= 7 and row_num - c >= 0:
                                    if self.board [row_num-c][col_num+c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num+c)))
                                        c = c+1
                                    elif self.board [row_num-c][col_num+c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num+c)))
                                        break
                                    else:
                                        break
                                
                            #knight
                            if part.piece == Piece.knight:
                                if row_num >=2:
                                    if col_num<=6:
                                        if self.board [row_num-2][col_num+1].piece == Piece.none or self.board [row_num-2][col_num+1].piece != Piece.none and self.board [row_num-2][col_num+1].is_white:
                                            moves.append(Move((row_num, col_num), (row_num-2,col_num+1)))
                                    if col_num>=1:
                                        if self.board [row_num-2][col_num-1].piece == Piece.none or self.board [row_num-2][col_num-1].piece != Piece.none and self.board [row_num-2][col_num-1].is_white:
                                            moves.append(Move((row_num, col_num), (row_num-2,col_num-1)))
                                if row_num >=1:
                                    if col_num<=5:
                                        if self.board [row_num-1][col_num+2].piece == Piece.none or self.board [row_num-1][col_num+2].piece != Piece.none and self.board [row_num-1][col_num+2].is_white:
                                            moves.append(Move((row_num, col_num), (row_num-1,col_num+2)))
                                    if col_num>=2:
                                        if self.board [row_num-1][col_num-2].piece == Piece.none or self.board [row_num-1][col_num-2].piece != Piece.none and self.board [row_num-1][col_num-2].is_white:
                                            moves.append(Move((row_num, col_num), (row_num-1,col_num-2)))
                                if row_num <=5:
                                    if col_num<=6:
                                        if self.board [row_num+2][col_num+1].piece == Piece.none or self.board [row_num+2][col_num+1].piece != Piece.none and self.board [row_num+2][col_num+1].is_white:    
                                            moves.append(Move((row_num, col_num), (row_num+2,col_num+1)))
                                    if col_num>=1:
                                        if self.board [row_num+2][col_num-1].piece == Piece.none or self.board [row_num+2][col_num-1].piece != Piece.none and self.board [row_num+2][col_num-1].is_white:
                                            moves.append(Move((row_num, col_num), (row_num+2,col_num-1)))
                                if row_num <=6:
                                    if col_num<=5:
                                        if self.board [row_num+1][col_num+2].piece == Piece.none or self.board [row_num+1][col_num+2].piece != Piece.none and self.board [row_num+1][col_num+2].is_white:
                                            moves.append(Move((row_num, col_num), (row_num+1,col_num+2)))
                                    if col_num>=2:
                                        if self.board [row_num+1][col_num-2].piece == Piece.none or self.board [row_num+1][col_num-2].piece != Piece.none and self.board [row_num+1][col_num-2].is_white:
                                            moves.append(Move((row_num, col_num), (row_num+1,col_num-2)))
                            #queen
                            if part.piece == Piece.queen:
                                c = 1
                                while row_num - c >= 0:
                                    if self.board [row_num-c][col_num].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num)))
                                        c = c+1
                                    elif self.board [row_num-c][col_num].is_white:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num)))
                                        break
                                    else:
                                        break
                                c = 1
                                while row_num + c <= 7: 
                                    if self.board [row_num+c][col_num].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num)))
                                        c = c+1
                                    elif self.board [row_num+c][col_num].is_white:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num)))
                                        break
                                    else:
                                        break
                                c = 1
                                while col_num - c >= 0:
                                    if self.board [row_num][col_num-c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num, col_num-c)))
                                        c = c+1
                                    elif self.board [row_num][col_num-c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num, col_num-c)))
                                        break
                                    else:
                                        break
                                c = 1
                                while col_num + c <= 7:
                                    if self.board [row_num][col_num+c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num, col_num+c)))
                                        c = c+1
                                    elif self.board [row_num][col_num+c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num, col_num+c)))
                                        break
                                    else:
                                        break                                    
                            if part.piece == Piece.bishop:
                                c = 1
                                while row_num - c >= 0 and col_num - c >= 0:
                                    if self.board [row_num-c][col_num-c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num-c)))
                                        c = c+1
                                    elif self.board [row_num-c][col_num-c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num-c)))
                                        break
                                    else:
                                        break

                                c = 1
                                while row_num + c <= 7 and col_num + c <= 7:
                                    if self.board [row_num+c][col_num+c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num+c)))
                                        c = c+1
                                    elif self.board [row_num+c][col_num+c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num+c)))
                                        break
                                    else:
                                        break
                                c = 1
                                while col_num - c >= 0 and row_num + c <= 7:
                                    if self.board [row_num+c][col_num-c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num-c)))
                                        c = c+1
                                    elif self.board [row_num+c][col_num-c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num+c, col_num-c)))
                                        break
                                    else:
                                        break
                                
                                c = 1
                                while col_num + c <= 7 and row_num - c >= 0:
                                    if self.board [row_num-c][col_num+c].piece == Piece.none:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num+c)))
                                        c = c+1
                                    elif self.board [row_num-c][col_num+c].is_white:
                                        moves.append (Move((row_num, col_num), (row_num-c, col_num+c)))
                                        break
                                    else:
                                        break
            return moves

        def get_king_moves (is_white):
            all_black_moves = get_not_king_moves(not is_white)
            all_white_moves = get_not_king_moves(is_white)
            def white_no_threat_form_not_kings_in (point):
                flag = True
                for move in all_black_moves:
                    if point == move.end :
                        flag = False
                        break
                return flag
            def black_no_threat_form_not_kings_in (point):
                flag = True
                for move in all_white_moves:
                    if point == move.end :
                        flag = False
                        break
                return flag            
            white_king_moves = []
            black_king_moves = []
            white_position = [None, None]
            black_position = [None, None]
            for row_num in range (8):
                for col_num in range (8):
                    part = self.board [row_num][col_num]
                    if part.piece != Piece.none:
                        #white
                        if part.is_white and is_white:
                            #king
                            if part.piece == Piece.king:
                                white_position = [row_num, col_num]
                                if row_num > 0:
                                    if white_no_threat_form_not_kings_in ((row_num-1, col_num)) and self.board [row_num-1][col_num].piece == Piece.none or self.board [row_num-1][col_num].piece != Piece.none and not self.board [row_num-1][col_num].is_white:
                                        white_king_moves.append ((row_num-1, col_num))
                                    if col_num > 0:
                                        if white_no_threat_form_not_kings_in ((row_num-1, col_num-1)) and self.board [row_num-1][col_num-1].piece == Piece.none or self.board [row_num-1][col_num-1].piece != Piece.none and not self.board [row_num-1][col_num-1].is_white:
                                            white_king_moves.append ((row_num-1, col_num-1))
                                    if col_num < 7:
                                        if white_no_threat_form_not_kings_in ((row_num-1, col_num+1)) and self.board [row_num-1][col_num+1].piece == Piece.none or self.board [row_num-1][col_num+1].piece != Piece.none and not self.board [row_num-1][col_num+1].is_white:
                                            white_king_moves.append ((row_num-1, col_num+1))
                                if col_num > 0:
                                    if white_no_threat_form_not_kings_in ((row_num, col_num-1)) and self.board [row_num][col_num-1].piece == Piece.none or self.board [row_num][col_num-1].piece != Piece.none and not self.board [row_num][col_num-1].is_white:
                                        white_king_moves.append ((row_num, col_num-1))                                                                    

                                if col_num < 7:
                                    if white_no_threat_form_not_kings_in ((row_num, col_num+1)) and self.board [row_num][col_num+1].piece == Piece.none or self.board [row_num][col_num+1].piece != Piece.none and not self.board [row_num][col_num+1].is_white:
                                        white_king_moves.append ((row_num, col_num+1))

                                if row_num < 7:
                                    if white_no_threat_form_not_kings_in ((row_num+1, col_num)) and self.board [row_num+1][col_num].piece == Piece.none or self.board [row_num+1][col_num].piece != Piece.none and not self.board [row_num+1][col_num].is_white:
                                        white_king_moves.append ((row_num+1, col_num))
                                    if col_num > 0:
                                        if white_no_threat_form_not_kings_in ((row_num+1, col_num-1)) and self.board [row_num+1][col_num-1].piece == Piece.none or self.board [row_num+1][col_num-1].piece != Piece.none and not self.board [row_num+1][col_num-1].is_white:
                                            white_king_moves.append ((row_num+1, col_num-1))
                                    if col_num < 7:
                                        if white_no_threat_form_not_kings_in ((row_num+1, col_num+1)) and self.board [row_num+1][col_num+1].piece == Piece.none or self.board [row_num+1][col_num+1].piece != Piece.none and not self.board [row_num+1][col_num+1].is_white:
                                            white_king_moves.append ((row_num+1, col_num+1))

                        #black
                        if not part.is_white and not is_white:
                            #king
                            if part.piece == Piece.king:
                                black_position = [row_num, col_num]
                                if row_num > 0:
                                    if black_no_threat_form_not_kings_in ((row_num-1, col_num)) and self.board [row_num-1][col_num].piece == Piece.none or self.board [row_num-1][col_num].piece != Piece.none and self.board [row_num-1][col_num].is_white:
                                        black_king_moves.append ((row_num-1, col_num))
                                    if col_num > 0:
                                        if black_no_threat_form_not_kings_in ((row_num-1, col_num-1)) and self.board [row_num-1][col_num-1].piece == Piece.none or self.board [row_num-1][col_num-1].piece != Piece.none and self.board [row_num-1][col_num-1].is_white:
                                            black_king_moves.append ((row_num-1, col_num-1))
                                    if col_num < 7:
                                        if black_no_threat_form_not_kings_in ((row_num-1, col_num+1)) and self.board [row_num-1][col_num+1].piece == Piece.none or self.board [row_num-1][col_num+1].piece != Piece.none and self.board [row_num-1][col_num+1].is_white:
                                            black_king_moves.append ((row_num-1, col_num+1))
                                if col_num > 0:
                                    if black_no_threat_form_not_kings_in ((row_num, col_num-1)) and self.board [row_num][col_num-1].piece == Piece.none or self.board [row_num][col_num-1].piece != Piece.none and self.board [row_num][col_num-1].is_white:
                                        black_king_moves.append ((row_num, col_num-1))                                                                    

                                if col_num < 7:
                                    if black_no_threat_form_not_kings_in ((row_num, col_num+1)) and self.board [row_num][col_num+1].piece == Piece.none or self.board [row_num][col_num+1].piece != Piece.none and self.board [row_num][col_num+1].is_white:
                                        black_king_moves.append ((row_num, col_num+1))

                                if row_num < 7:
                                    if black_no_threat_form_not_kings_in ((row_num+1, col_num)) and self.board [row_num+1][col_num].piece == Piece.none or self.board [row_num+1][col_num].piece != Piece.none and self.board [row_num+1][col_num].is_white:
                                        black_king_moves.append ((row_num+1, col_num))
                                    if col_num > 0:
                                        if black_no_threat_form_not_kings_in ((row_num+1, col_num-1)) and self.board [row_num+1][col_num-1].piece == Piece.none or self.board [row_num+1][col_num-1].piece != Piece.none and self.board [row_num+1][col_num-1].is_white:
                                            black_king_moves.append ((row_num+1, col_num-1))
                                    if col_num < 7:
                                        if black_no_threat_form_not_kings_in ((row_num+1, col_num+1)) and self.board [row_num+1][col_num+1].piece == Piece.none or self.board [row_num+1][col_num+1].piece != Piece.none and self.board [row_num+1][col_num-1].is_white:
                                            black_king_moves.append ((row_num+1, col_num+1))

            final_king_moves = []
            if is_white:
                for tup in white_king_moves:
                    if not (tup in black_king_moves):
                        final_king_moves.append (Move((white_position[0], white_position[1]), tup))
            if not is_white:
                for tup in black_king_moves:
                    if not (tup in white_king_moves):
                        final_king_moves.append (Move((black_position[0], black_position[1]), tup))
            return final_king_moves

        #return get_not_king_moves(is_white) + get_king_moves(is_white)                            
        return get_not_king_moves(is_white)

    def check_move(self, move, is_white):
        for m in self.all_moves (is_white):
            if move.start == m.start and move.end == m.end:
                return True
        return False


    def do_move(self, move, is_white):
        sr, sc = move.start
        er, ec = move.end
        self.board[er][ec].piece = self.board[sr][sc].piece
        self.board[er][ec].is_white = self.board[sr][sc].is_white
        self.board[sr][sc].is_white = None
        self.board[sr][sc].piece = Piece.none


    def is_check(self, is_white):
        for row in range(8):
            for col in range(8):
                if self.board[row][col].piece == Piece.king and self.board[row][col].is_white == is_white:
                    king_position = (row, col)
                    break
        enemy_moves = self.all_moves (not self.board[king_position[0]][king_position[1]].is_white)
        for move in enemy_moves:
            if king_position == move.end:
                return True
        return False


    def is_mate(self, is_white):
        return False

