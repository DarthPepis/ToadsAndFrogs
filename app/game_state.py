from typing import List

#tah jako uspořadana dvojice, pouze uložim, pak použivam
class Move:
    def __init__(self, from_idx, to_idx):
        self.from_idx = from_idx
        self.to_idx = to_idx

    #funkce na vypsani find_best_move()
    def __repr__(self):
        return f"Move(from_idx = {self.from_idx}, to_idx = {self.to_idx})"

class GameState:
    def __init__(self, board: List[str], current_player: int = 1):
        self.board = board
        self.current_player = current_player

    def clone(self):
        return GameState(self.board.copy(), self.current_player)
    #vraci GameState na kopii boardu, jinak bychom měnili ten aktualni board při každem tahu AI

    def is_terminal(self): #vraci True/False
        return len(self.generate_moves()) == 0
    

    #přidavame tahy do pole
    def generate_moves(self) -> List[Move]:
        moves = []
        if self.current_player == 1:
            piece = 'T'
            direction = 1
        else:
            piece = 'F'
            direction = -1

        for i, cell in enumerate(self.board):
            if cell == piece:
                #pokud btn na board je piece ktery chceme
                # krok
                target = i + direction
                if 0 <= target < len(self.board) and self.board[target] == '.':
                    moves.append(Move(i, target))

                # skok
                jump_over = i + direction #pole přes ktere skaču
                jump_to = i + 2 * direction #na ktere skaču

                #přidame dalši moves ktere jsou jump
                if (
                    0 <= jump_over < len(self.board)
                    and 0 <= jump_to < len(self.board)
                    and self.board[jump_over] in ('T', 'F')
                    and self.board[jump_to] == '.'
                ):
                    moves.append(Move(i, jump_to)) #tedy každy prvek pole moves je jedna instance třidy Move

        return moves

    def apply_move(self, move): #chceme move jako uspořadanou dvojici, v gui mame zadefinovano
        new_state = self.clone() #dělam klon
        piece = new_state.board[move.from_idx] #beru figurku 
        new_state.board[move.from_idx] = '.' #pokladam misto figurky '.'
        new_state.board[move.to_idx] = piece #na target davam piece
        new_state.current_player = 2 if self.current_player == 1 else 1 #změna players
        return new_state #vracim instanci GameState 
 
