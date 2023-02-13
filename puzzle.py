"""
There are 3 functions, that helped us to write the last main function
https://github.com/Nastunya04/puzzle_task.git
Матвісів Уляна
Дмитрів Христина
Диня Анастасія
"""
def check_rows(board):
    """
    >>> check_rows([\
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
    return True

def check_colours(lst):
    """
    Function checks if all numbers in the same colour on board are unique.
    If it is so, function returns True/else: returns False
    >>> check_colours(["**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 2 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"])
    True
    """
    i = len(lst) // 2
    j = i + 1
    num = 0
    k = 9
    while k != 4:
        new_lst = []
        for board1 in lst[num:j]:
            board1k =  board1[i:k]
            new_lst.append(board1k)
        k -= 1
        i -= 1
        num += 1
        j += 1
        boardk = []
        dct = {}
        for numb in range(len(new_lst) - 1):
            boardk.append(new_lst[numb][0])
        for smth in new_lst[-1]:
            boardk.append(smth)
        new_boardk = [elem for elem in boardk if elem.isnumeric()]
        dct = {elem:new_boardk.count(elem) for elem in new_boardk}
        for number in dct.values():
            if number != 1:
                return False
    return True

def validate_board(board):
    """Function checks if game field is filled in the right way.
    (Verticals,horisontals and figures of the same colour have unique numbers)
    >>> validate_board(["****7****",\
"***17****",\
"**  3****",\
"* 4 1****",\
"     9 2 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"])
    False
    """
    return check_rows(board) and check_vertical(board) and check_colours(board)

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
