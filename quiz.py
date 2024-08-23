def reverse_list(l: list):
    """

    TODO: Reverse a list without using any built in functions

    The function should return a sorted list.

    Input l is a list which can contain any type of data.

    """
    reversed_list = []
    for i in range(len(l) - 1, -1, -1):
        reversed_list.append(l[i])
    return reversed_list


def solve_sudoku(matrix):
    """

    TODO: Write a programme to solve 9x9 Sudoku board.



    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.



    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    """
    def check_valid(board, row, col, num):
        # Check curr row, column 3x3 number or not 
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
            if board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] == num:
                return False
        return True

    tmp = [] #make stack save checked number
    grid = [(row, col) for row in range(9) for col in range(9) if matrix[row][col] == 0] #make matrix
    i = 0

    while i < len(grid):
        row, col = grid[i]
        num = matrix[row][col] + 1 #try number
        check = False

        while num <= 9:
            if check_valid(matrix, row, col, num):
                matrix[row][col] = num
                tmp.append((row, col, num))
                check = True
                break
            num += 1

        if check:
            i += 1
        else:
            if not tmp:
                return False  # No solution
            row, col, num = tmp.pop()
            matrix[row][col] = 0
            i -= 1

    return matrix
    
    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if check_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    #solve(matrix)
    return matrix
    