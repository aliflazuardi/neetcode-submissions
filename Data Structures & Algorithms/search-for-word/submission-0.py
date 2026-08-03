class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def backtracking(i, r, c):
            if i == len(word):
                return True 
            
            # check for boundary and not matching character
            if r < 0 or c < 0  or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path:
                return False
            
            path.add((r, c))
            ans = (backtracking(i + 1, r + 1, c) or 
            backtracking(i + 1, r - 1, c) or
            backtracking(i + 1, r, c + 1) or 
            backtracking(i + 1, r, c - 1))
            path.remove((r, c))
            return ans
    
        for r in range(ROWS):
            for c in range(COLS):
                    if backtracking(0, r, c):
                        return True
        return False