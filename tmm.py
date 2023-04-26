def create_position(col, lin):
     """
     This function takes two strings of characters corresponding to
     column and row of a position and returns the corresponding position.
     """
     col_to_num = {
         'a': 1,
         'b': 2,
         'c': 3
     }
     if type(col) == type(lin) == str:
         if col in col_to_num and lin in ('1','2','3'):
             return [col_to_num[col] + 3*(int(lin)-1)]
     raise ValueError('create_position: Invalid arguments')


def create_copy_position(pos):
     """
     This function receives a position and returns a new copy
     of the position.
     """
     return [pos[0]]


def get_pos_c(pos):
     """
     This function returns the column component of the position.
     """
     if pos[0] in (1, 4, 7):
         return 'a'
     elif pos[0] in (2, 5, 8):
         return 'b'
     elif pos[0] in (3, 6, 9):
         return 'c'


def get_pos_l(pos):
     """
     This function returns the line component of the position.
     """
     if pos[0] in (1, 2, 3):
         return '1'
     elif pos[0] in (4, 5, 6):
         return '2'
     elif pos[0] in (7, 8, 9):
         return '3'


def is_posicao(pos):
     """
     This function returns True if its argument is a TAD
     position and False otherwise.
     """
     return type(pos) == list and type(pos[0]) == int and 0 < pos[0] < 10

def equal_positions(pos1, pos2):
     """
     This function returns True only if pos1 and pos2 are positions
     and are equal.
     """
     return is_posicao(pos1) and is_posicao(pos2) and pos1 == pos2

def position_to_str(pos):
     """
     This function returns the 'cl' character string that represents the
     its argument, with the values c and l being the column and row components
     of pos.
     """
     return get_pos_c(pos) + get_pos_l(pos)


def get_adjacent_positions(pos):
     """
     This function returns a tuple with the positions adjacent to the position
     according to the reading order of the board.
     """
     adj_aux = {
         'a1': ('b1', 'a2', 'b2'),
         'b1': ('a1', 'c1', 'b2'),
         'c1': ('b1', 'b2', 'c2'),
         'a2': ('a1', 'b2', 'a3'),
         'b2': ('a1', 'b1', 'c1', 'a2', 'c2', 'a3', 'b3', 'c3'),
         'c2': ('c1', 'b2', 'c3'),
         'a3': ('a2', 'b2', 'b3'),
         'b3': ('b2', 'a3', 'c3'),
         'c3': ('b2', 'c2', 'b3')
     }
     pos_adj = ()
     for e in adj_aux[position_to_str(pos)]:
         pos_adj += create_position(e[0], e[1]),
     return pos_adj



def create_piece(jog):
     """
     This function receives a string of characters corresponding to the identifier
     one of the players ('X' or 'O') or to a free piece (' ') and returns the
     corresponding part.
     """
     piece_aux = {
         'X': 1,
         'O': -1,
         ' ': 0
     }
     if type(jog) == str and jog in piece_aux:
         return [piece_aux[jog]]
     raise ValueError('create_part: Invalid argument')


def create_copy_piece(piece):
     """
     This function receives a part and returns a new copy of the part.
     """
     return piece.copy()


def is_piece(piece):
     """
     This function returns True if its argument is a TAD piece and False if
     contrary.
     """
     return type(piece) == list and len(piece) == 1 and \
            type(piece[0]) == int and piece[0] in (-1, 0, 1)


def equal_pieces(piece1, piece2):
     """
     This function returns True even if piece1 and piece2 are pieces and are equal.
     """
     return is_piece(piece1) and is_piece(piece2) and piece1 == piece2


def piece_to_str(piece):
     """
     This function returns the character string that represents the player who owns the
     part.
     """
     piece_str_aux = {
         1: '[X]',
         -1: '[O]',
         0: '[ ]'
     }
     return piece_str_aux[piece[0]]


def piece_to_integer(piece):
     """
     This function returns an integer (-1, 1, or 0), depending on whether the part is from
     player 'X', 'O' or free, respectively.
     """
     aux_integer_piece = {
         '[X]': 1,
         '[O]': -1,
         '[ ]': 0
     }
     return aux_integer_piece[piece_to_str(piece)]


def create_board():
     """
     This function returns a 3x3 tmm game board with no occupied positions
     for player parts.
     """
     p_free = create_piece(' ')
     return [[p_free, p_free, p_free], [p_free, p_free, p_free], \
         [p_free, p_free, p_free]]


def create_copy_board(tab):
     """
     This function receives a board and returns a new copy of the board.
     """
     copy_tab = create_board()
     for i in range(3):
         for i2 in range(3):
             if not equal_pieces(tab[i][i2], copy_tab[i][i2]):
                 copy_tab[i][i2] = create_copy_piece(tab[i][i2])
     return copy_tab
 

def get_piece(tab, pos):
     """
     This function returns the piece to the pos position on the board. If the position does not
     is occupied, it returns a free position.
     """
     return tab[int(get_pos_l(pos))-1][column_to_num(get_pos_c(pos))-1]


def get_vector(tab, vet):
     """
     This function returns all parts of the row or column specified by the
     your argument.
     """
     if vet in('1', '2', '3'):
         return tuple(tab[int(vet)-1])
     else:
         column_num = column_to_num(vet) - 1
         return (tab[0][column_num], tab[1][column_num], tab[2][column_num])


def place_piece(tab, piece, pos):
     """
     This function destructively modifies the tab board by placing the piece piece
     in position pos, and returns the board itself.
     """
     tab[int(get_pos_l(pos))-1][column_to_num(get_pos_c(pos))-1] = piece
     return tab


def remove_piece(tab, pos):
     """
     This function destructively modifies the tab board by removing the tile from the
     pos position, and returns the board itself.
     """
     place_piece(tab, create_piece(' '), pos)
     return tab


def move_piece(tab, pos1, pos2):
     """
     This function destructively modifies the tab board by moving the piece that moves
     finds in position pos1 to position pos2, and returns the board itself.
     """
     piece_moved = get_piece(tab, pos1)
     remove_piece(tab, pos1)
     place_piece(tab, piece_moved, pos2)
     return tab


def is_tabuleiro(tab):
     """
     This function returns True if its argument is a TAD board and False
     otherwise.
     """
     count_jog1 = count_jog2 = count_winner = 0
     if type(tab) != list or len(tab) != 3:
         return False
     for e in tab:
         if type(e) != list or len(e) != 3:
             return False
         for e2 in e:
             if equal_pieces(e2, create_piece('O')):
                 count_jog1 += 1
             elif equal_pieces(e2, create_piece('X')):
                 count_jog2 += 1
             elif not equal_pieces(e2, create_piece(' ')):
                 return False
     if count_jog1 > 3 or count_jog2 > 3:
         return False
     if abs(count_jog1 - count_jog2) > 1:
         return False
     for e in ('abc123'):
         if equal_pieces(get_vector(tab, e)[0], get_vector(tab, e)[1]) \
            and equal_pieces(get_vector(tab, e)[2], get_vector(tab, e)[1])\
            and not equal_pieces(get_vector(tab, e)[0], create_piece(' ')):
             count_winner += 1
     return count_winner < 2

                
def is_free_position(tab, pos):
     """
     This function returns True only in the case of position p on the board
     correspond to a free position.
     """
     return equal_pieces(get_piece(tab, pos), create_piece(' '))


def equal_boards(tab1, tab2):
     """
     This function returns True only if tab1 and tab2 are boards and are equal.
     """
     if not (is_tabuleiro(tab1) and is_tabuleiro(tab2)):
         return False
     for i in range(3):
         for i2 in range(3):
             if not equal_pieces(tab1[i][i2], tab2[i][i2]):
                 return False
     return true



def board_to_str(tab):
     """
     This function returns the character string that represents the board.
     """
     count = 0
     string = '   a   b   c\n1 '
     for e in tab:
         for e2 in e:
             if equal_pieces(e2, create_piece('X')):
                 string += '[X]-'
             elif equal_pieces(e2, create_piece('O')):
                 string += '[O]-'
             elif equal_pieces(e2, create_piece(' ')):
                 string += '[ ]-'
         string = string[:len(string) - 1]
         if count == 0:
             string += '\n   | \\ | / |\n2 '
             count += 1
         elif count == 1:
             string += '\n   | / | \\ |\n3 '
             count += 1
     return string


def tuple_to_board(tup):
     """
     This function returns the board that is represented by the tuple tup with 3
     tuples, each containing 3 integer values equal to 1, -1, or 0.
     """
     tuplo_p_tab_aux = {
         -1: 'O',
         0: ' ',
         1: 'X'
     }
     tab = create_board()
     for i in range(3):
         for i2 in range(3):
             tab[i][i2] = create_piece(tuplo_p_tab_aux[tup[i][i2]])
     return tab
def get_winner(tab):
     """
     This function returns a piece of the player whose 3 pieces are in line
     vertically or horizontally on the board. If there is no winner,
     returns a free piece.
     """
     for e in('abc123'):
         if equal_pieces(get_vector(tab, e)[0], get_vector(tab, e)[1]) and \
            equal_pieces(get_vector(tab, e)[1], get_vector(tab, e)[2]) and not\
            equal_pieces(get_vector(tab, e)[0], create_piece(' ')):
            return get_vector(tab, e)[0]
     return create_piece(' ')


def get_free_positions(tab):
     """
     This function returns a tuple with the positions not occupied by the pieces of
     either of the two players in the order read on the board.
     """
     return get_player_positions(tab, create_piece(' '))


def get_player_positions(tab, piece):
     """
     This function returns a tuple with the positions occupied by the parts part of a
     of the two players in the order read on the board.
     """
     post_jog =()
     get_pos_jog_aux = {
         0: 'a',
         1: 'b',
         2: 'c'
     }
     for e in('123'):
         for i in range(3):
             if equal_pieces(get_vector(tab, e)[i], piece):
                 post_jog += (create_position(get_pos_jog_aux[i], e),)
     return post_jog


def get_manual_movement(tab, piece):
     """
     This function receives a board and a piece, and returns a tuple that
     represents a position or a movement entered manually by the player.
     """
     col = ('a', 'b', 'c')
     lin = ('1', '2', '3')
     if len(get_player_positions(tab, piece)) < 3:
         pos = input('Player\'s turn. Choose a position:')
         if len(pos) == 2 and pos[0] in col and pos[1] in lin:
             if is_free_position(tab, create_position(pos[0], pos[1])):
                 return (create_position(pos[0], pos[1]),)
         raise ValueError('get_manual_movement: invalid choice')
     pos = input('Player\'s turn. Choose a move: ')
     if len(pos) == 4 and pos[0] in col and pos[1] in lin \
        and pos[2] in col and pos[3] in lin:
         pos1 = create_position(pos[0], pos[1])
         pos2 = create_position(pos[2], pos[3])
         if equal_pieces(get_piece(tab, pos1), piece)\
            and is_free_position(tab, pos2) and is_position_adjacent(pos1, pos2):
             return(pos1, pos2)
         mov_poss = 0
         for e in get_player_positions(tab, piece):
             for e2 in get_adjacent_positions(e):
                 if is_free_position(tab, e2):
                     mov_poss += 1
         if mov_poss == 0 and positions_equal(pos1, pos2):
             return(pos1, pos2)
     raise ValueError('get_manual_movement: invalid choice')





def get_auto_movement(tab, piece, level):
     """
     get_auto_movement: board x piece x string -> tuple of positions
     This function receives a board, a piece and a string representing the level
     of game difficulty, and returns a tuple that represents a position or a
     move chosen automatically.
     """
     pos_jog = get_player_positions(tab, piece)
     res_minimax = 0
     if len(pos_jog) < 3:
         set_pos = [
                 win(tab, piece),
                 lock(tab, piece),
                 center(tab),
                 empty_corner(tab),
                 empty_side(tab)
             ]
         for e in set_pos:
             if is_posicao(e):
                 return(e,)
     elif level == 'Easy':
         for e in pos_jog:
             for e2 in get_adjacent_positions(e):
                 if is_free_position(tab, e2):
                     return(e, e2)
         return (pos_jog[0], pos_jog[0])
     elif level == 'Normal':
         res_minimax = minimax(tab, piece, 1, ())
     elif level == 'Difficult':
         res_minimax = minimax(tab, piece, 5, ())
     if res_minimax != 0:
         if len(res_minimax[1]) > 1:
             return res_minimax[1][0], res_minimax[1][1]
         return (pos_jog[0], pos_jog[0])


def tmm(piece, level):
     """
     tmm: string x string -> string
     This function allows you to play a complete game of the tmm game against the
     computer.
     """
     if (piece == '[X]' or piece == '[O]') and \
        (level == 'Easy' or level == 'Normal' or level == 'Difficult'):
         piece = create_piece(piece[1])
         p_contrary = counter_piece(piece)
         print('Welcome to the Three Men Morris Game.\nDifficulty level '+ level +'.')
         tab = create_board()
         game_current = 1
         print(board_to_str(tab))
         while equal_pieces(get_winner(tab), create_piece(' ')):
             if game_current == piece_to_integer(piece):
                 mov = get_manual_movement(tab, piece)
                 if len(get_player_positions(tab, piece)) < 3:
                     tab = place_piece(tab, piece, mov[0])
                 else: tab = move_piece(tab, mov[0], mov[1])
             else:
                 print('Computer turn:')
                 move_auto = get_auto_movement(tab, p_contrary, level)
                 if len(get_player_positions(tab, p_contrary)) < 3:
                     tab = place_piece(tab, p_contrary, move_auto[0])
                 else: tab = move_piece(tab, move_auto[0], move_auto[1])
             print(board_to_str(tab))
             game_current = -game_current
         return piece_to_str(get_winner(tab))
     raise ValueError('tmm: invalid arguments')


# extra helper functions
def win(tab, piece):
     """
     win: board x piece -> position
     This function receives a board and a piece identifying a player.
     If a win is possible, it returns the position that guarantees the win.
     """
     for pos in get_free_positions(tab):
         new_tab = place_piece(create_copy_board(tab), piece, pos)
         if equal_pieces(get_winner(new_tab), piece):
             return pos


def lock(tab, piece):
     """
     lock: board x piece -> position
     This function receives a board and a piece identifying a player and case
     an opponent's victory is imminent, returns the position that blocks the
     victory.
     """
     return win(tab, counter_piece(piece))


def center(tab):
     """
     center: board -> position
     This function receives a board and if the central position is empty
     return the same.
     """
     if is_free_position(tab, create_position('b', '2')):
         return create_position('b', '2')


def empty_corner(tab):
     """
     corner_empty: board -> position
     This function receives a board and if one of the corners is empty it returns
     the same.
     """
     corners = [create_position('a', '1'), create_position('c', '1'), \
              create_position('a', '3'), create_position('c', '3')]
     for e in corners:
         if is_free_position(tab, e):
             return e


def empty_side(tab):
     """
     corner_empty: board -> position
     This function receives a board and if one of the sides is empty
     return the same.
     """
     laterals = [create_position('b', '1'), create_position('a', '2'), \
              create_position('c', '2'), create_position('b', '3')]
     for e in laterals:
         if is_free_position(tab, e):
             return e


def minimax(tab, piece, prof, seq_mov):
     """
     minimax: board, piece, depth, seq. moves -> tuple of values
     This function exploits all legal moves of the player using the piece.
     asks for a defined depth and returns the movement that favors the most
     this player.
     """
     if not equal_pieces(get_winner(tab), create_piece(' ')) or prof == 0:
         return (piece_to_integer(get_winner(tab)), seq_mov)
     else:
         best_res = piece_to_integer(counter_piece(piece))
         best_seq_mov = ()
         for pos in get_player_positions(tab, piece):
             for pos_adj in get_adjacent_positions(pos):
                 if is_free_position(tab, pos_adj):
                     new_t = move_piece(create_copy_board(tab), pos, pos_adj)
                     new_res, new_seq_mov = minimax(new_t, \
                     counter_piece(piece), prof-1, seq_mov + (pos, pos_adj))
                     if best_seq_mov == () or \
                        (equal_pieces(piece, create_piece('X')) and
                        new_res > best_res) or \
                        (equal_pieces(piece, create_piece('O')) and
                        new_res < best_res):
                         best_res, best_seq_mov = new_res, new_seq_mov
         return best_res, best_seq_mov

def counter_piece(piece):
     """
     pec_contraria: pec -> pec
     This function receives a player's piece and returns the opposite player's piece.
     """
     counter_piece = {
         '[X]': 'O',
         '[O]': 'X'
     }
     return create_piece(counter_piece[piece_to_str(piece)])


def column_to_num(col):
     """
     column_to_num: string -> integer
     This function receives a string that represents one of the three columns of the
     board and returns the column number, counting from left to right.
     """
     col_num = {
         'a': 1,
         'b': 2,
         'c': 3
     }
     return col_num[col]


def is_position_adjacent(pos1, pos2):
     """
     is_position_adjacent: position x position -> boolean
     This function receives two positions and returns True if they are adjacent positions
     and False otherwise.
     """
     for e in get_adjacent_positions(pos1):
         if equal_positions(pos2, e):
             return True
     return False

def main():
    print("---- Welcome Player ----- \n")
    print("Choose your difficulty level(Enter number only: \n1. Easy\n2. Normal\n3. Hard")
    k = int(input())
    if(k==1):
        tmm('[X]','Easy')
    elif(k==2):
        tmm('[X]','Normal')
    elif(k==3):
        tmm('[X]','Difficult')
    else:
        print('Invalid Input!!\nExitting')
        exit()    
    
    print("\nThank you for playing")


if __name__ == "__main__":
    main()