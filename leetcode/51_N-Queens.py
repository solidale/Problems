chessboard = [
    ".Q..",
    "Q...",
    "...",
    "...Q"
]

def is_valid_state(chessboard: list[str]):
    for current_row, row in enumerate(chessboard):
        if row.count("Q") > 1:
            print(f"more than 1 queen in row {current_row}")
            return False
        for index, character in enumerate(row):
            if character == "Q":
                queen_position = (current_row, index)
                for i in range(len(chessboard)):
                    if i != queen_position[0]:
                        if chessboard[i][queen_position[1]] == "Q":
                            print(f"more than 1 queen in column {index}")
                            return False
                        if 0 <= queen_position[1] - queen_position[0] + i < len(chessboard) and chessboard[i][queen_position[1] - queen_position[0] + i] == "Q":
                            return False
                        if 0 <= queen_position[1] + queen_position[0] - i < len(chessboard) and chessboard[i][queen_position[1] + queen_position[0] - i] == "Q":
                            return False
    return True
print(is_valid_state(chessboard))

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        solutions = []
        state = [] 
        self.search(state, solutions, n)
        return solutions
    
    def search(self, state: list[int], solutions, n: int):
        if self.is_valid_state(state):
            solutions.append(state.copy())
        
        for candidate in get_candidates(state, n):
            state.add(candidate)
            self.search(state, solutions, n)
            state.remove(candidate)

    def is_valid_solution(self, state: list[int], n: int):
        # solution is valid if all n queens are on the chessboard
        return len(state) == n
    

    def get_candidates(self, state, n):
        if not state:
            return range(n)
        
        # find next position in state to populate
        
        return []