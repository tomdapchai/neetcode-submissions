class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # by row
        # by column
        for i in range(9):
            row_hash = [0] * 9
            for x in board[i]:
                if x == ".":
                    continue
                if row_hash[int(x) - 1]:
                    return False
                row_hash[int(x) - 1] += 1
            col_hash = [0] * 9
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if col_hash[int(board[j][i]) - 1]:
                    return False
                col_hash[int(board[j][i]) - 1] += 1
            if i % 3 == 0:
                # group 1
                g1_hash = [0] * 9
                for j in range(3):
                    for x in range(3):
                        if board[j][i + x] == ".":
                            continue
                        if g1_hash[int(board[j][i + x]) - 1]:
                            return False
                        g1_hash[int(board[j][i + x]) - 1] += 1
                # group 2
                g2_hash = [0] * 9
                for j in range(3, 6):
                    for x in range(3):
                        if board[j][i + x] == ".":
                            continue
                        if g2_hash[int(board[j][i + x]) - 1]:
                            return False
                        g2_hash[int(board[j][i + x]) - 1] += 1
                # group 3
                g3_hash = [0] * 9
                for j in range(6, 9):
                    for x in range(3):
                        if board[j][i + x] == ".":
                            continue
                        if g3_hash[int(board[j][i + x]) - 1]:
                            return False
                        g3_hash[int(board[j][i + x]) - 1] += 1
        # by 3x3 area

        return True

        