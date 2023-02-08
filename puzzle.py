def third_function(lst):
    """
    Function checks if all numbers in the same colour on board are unique.
    If it is so, function returns True/else: returns False
    >>> third_function(["**** ****",\
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
    i = 4
    j = 5
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
    return first_function(board) and check_vertical(board) and third_function(board)
