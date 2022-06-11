

from typing import Tuple, List
BOARD = List[List[str]]
CELLS_LIST = List[Tuple[int, int]]
VALID_DIR = {"L": (0, -1),
             "R": (0, 1),
             "U": (-1, 0),
             "D": (1, 0),
             "UL": (-1, -1),
             "UR": (1, -1),
             "DL": (-1, 1),
             "DR": (1, 1)}


def valid_cells(board) -> List[Tuple[int, int]]:
    """
    Returns list of cells for a given board
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
    cells = valid_cells(board)
    for tup in path:
        if tup not in cells:
            return True
    return False


def is_valid_path(board, path, words):
    """
    The function returns word if the path is valid, and the word
    appears in the words container
    :param board: board
    :param path: path of cells
    :param words: words bank
    :return: str(word), :returns: None
    """
    if is_path_outside_the_board(path, board) or len(path) == 0:
        return None
    # check for valid moves by distance (like vertical,horizontal and diagonal)
    letters = [board[path[0][0]][path[0][1]]]
    stepped_cells = [path[0]]

    for cell in path[1:]:
        distance = ((cell[0] - stepped_cells[-1][0]) ** 2 +
                    (cell[1] - stepped_cells[-1][1]) ** 2) ** 0.5
        if distance != 1 and distance != 2**0.5:
            return None
        if cell in stepped_cells:
            return None
        letters.append(board[cell[0]][cell[1]])
        stepped_cells.append(cell)
    word = "".join(letters)
    if word in words:
        return word
    else:
        return None


def valid_word(word: str, valid_chars: List[str]):
    """
    This function checks if a word in the word bank is valid (according to the board)
    :param word:
    :param valid_chars:
    :return:
    """
    # this list is a list of True-s and False-s for each letter in word.
    chars_in_valid_chars_bool_lst = [c in valid_chars for c in word]
    # this expression checks if there is false in the list. and returns the result
    return filter(lambda x,y: x and y, chars_in_valid_chars_bool_lst)


def find_n_path_rec(n: int, board: BOARD, cur_path: CELLS_LIST,
                    val_cells: CELLS_LIST) -> CELLS_LIST:
    """
    This function returns n-sized list contains cells of the board
    :param val_cells: list of valid cells.
    :param cur_path: list of current path we moved
    :param n: length og the word
    :param board: board.
    :return: List of valid-n-length-paths words.
    """



def find_length_n_paths(n, board, words):
    """
    This function returns
    :param n: int of
    :param board:
    :param words:
    :return:
    """
    VAL_CELLS = valid_cells(board)
    BOARD_ROWS = len(board)
    BOARD_COLS = len(board[0])
    valid_chars = []
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            valid_chars.append(board[row][col])
    res = []
    # this function keeps each of the words with length n and if each of the chars exists in the board.
    words_list = [word for word in words if len(word) == n and
                  valid_word(word, valid_chars)]
    for cell in valid_cells(board):
        res.extend(find_n_path_rec(n, board, [cell],VAL_CELLS))




def find_length_n_words(n, board, words):
    pass

def max_score_paths(board, words):
    pass
