

from typing import Tuple, List

VALID_DIR = {"L":(0,-1),
             "R":(0,1),
             "U":(-1,0),
             "D":(1,0),
             "UL":(-1,-1),
             "UR":(1,-1),
             "DL":(-1,1),
             "DR":(1,1)}


def valid_cells(board) -> List[Tuple[int, int]]:
    """
    Returns the cells of a given board
    :param board: board.
    :return: list of cells(tuple of 2 ints)
    """
    cells = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            cells.append((i,j))
    return cells


def is_path_outside_the_board(path, board) -> bool:
    """
    This function checks for each cell if its outside the board.
    :param path:
    :param board:
    :return:
    """
    cells  = valid_cells(board)
    for tup in path:
        if tup not in cells:
            return True
    return False


def is_valid_path(board, path, words):
    """The function :returns str (word) if the path is valid, and the word
    appears in the words container. else - it :return None"""
    if is_path_outside_the_board(board, path):
        return None
    # check for valid moves by distance (like vertical,horizontal and diagonal)
    letters = []
    stepped_cells = [path[0]]

    for cell in path[1:]:
        distance = ((cell[0] - stepped_cells[-1][0]) ** 2 +
                    (cell[1] - stepped_cells[-1][1]) ** 2) ** 0.5
        if distance != 1 and distance != 2**0.5:
            return None
        if cell in stepped_cells:
            return None
        letters.append(board.board[cell[0][1]])
        stepped_cells.append(cell)
    word = "".join(letters)
    if word in words:
        return word
    else:
        return None


def find_length_n_paths(n, board, words):
    """
    This function returns
    :param n:
    :param board:
    :param words:
    :return:
    """
    res = []
    words_dict = {}
    for word in words:
        length = len(word)
        if length not in words_dict:
            words_dict.update({length: [word]})
        words_dict.update({len{word}:})



def find_length_n_words(n, board, words):
    pass

def max_score_paths(board, words):
    pass
