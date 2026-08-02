class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            s=set()
            for j in i:
                if j == '.':
                    continue

                if j in s:
                    return False

                s.add(j)

        for i in range(len(board)):
            s2=set()
            for j in range(len(board)):

                if board[j][i] =='.':
                    continue
                if board[j][i] not in s2:
                    s2.add(board[j][i])
                else:
                    return False

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                s = set()

                for i in range(row, row + 3):
                    for j in range(col, col + 3):

                        if board[i][j] == '.':
                            continue

                        if board[i][j] in s:
                            return False

                        s.add(board[i][j])
                
        return True

        

        
