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
