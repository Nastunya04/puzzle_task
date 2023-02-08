"""
There are 3 functions, that helped us to write the last main function
https://github.com/Nastunya04/puzzle_task.git
Матвісів Уляна
Дмитрів Христина
Диня Анастасія
"""
def first_function(board):
    """
    >>> first_function([\
    "**** ****",\
    "***1 ****",\
    "  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  ",\
    "  8  2***",\
    "  2  ****"\
    ])
    True
    """
    for i in board:
        lst = [j for j in i if j!= "*" and j!= " "]
        check = [i.count(j) == 1 for j in lst]
        if not all(check) or len(lst) > 9:
            return False
    return True

def check_vertical(board):
    """This function checks if vertical of the board doesn`t contain same
    numbers and returns True.
    >>> check_vertical(["**** ****",\
    "***1 ****", "**  3****", "* 4 1****",\
    "     9 5 ", " 6  83  *", "3   1  **",\
    "  8  2***", "  2  ****"])
    False
    >>> check_vertical(["****2****",\
    "***14****", "**  7****", "* 3 9****",\
    "1    6 5 ", " 7  38  *", "3   1  **",\
    "  8   ***", "  1  ****"])
    True
    >>> check_vertical(["****1****",\
    "***1 ****", "**527****", "* 4 2****",\
    " 5   813 ", " 6  83  *", "9 6 5  **",\
    "  8  2***", "  2  ****"])
    True
    >>> check_vertical(["**** ****",\
    "***2 ****", "**   ****", "* 7 6****",\
    " 449 732 ", " 8  52  *", "2 3 6  **",\
    "  6  1***", "     ****"])
    False"""
    for i in range(9):
        lst = []
        for j in range(9):
            if board[j][i].isnumeric():
                if board[j][i] not in lst:
                    lst.append(board[j][i])
                else:
                    return False
