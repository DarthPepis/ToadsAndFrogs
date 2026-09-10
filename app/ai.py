#hodnotici funkce, kladne čislo vyhoda hrače - toads, zaporne AI
#vratime součet hodnot z celeho stavu
def evaluate(state):
    score = 0
    for i, cell in enumerate(state.board):
        if cell == 'T':
            score += i
        elif cell == 'F':
            score -= i
    return score


def alphabeta(state, depth, alpha, beta):
    # konec hry nebo konec hloubky
    if depth == 0 or state.is_terminal():
        return evaluate(state), None #tuple hodnota dvojice a tah ktery na něj vede

    moves = state.generate_moves() #všechny aktualni tahy v danem stavu

    if state.current_player == 'F':
        # AI = Frogs = maximalizuje
        best_value = float('-inf')
        best_move = None

        for move in moves:
            new_state = state.apply_move(move)
            value, _ = alphabeta(new_state, depth - 1, alpha, beta) 

            if value > best_value:
                best_value = value
                best_move = move

            alpha = max(alpha, value)
            if beta <= alpha:
                break  # alfa-beta ořezání

        return best_value, best_move

    else:
        # Hráč = Toads = minimalizuje
        best_value = float('inf')
        best_move = None

        for move in moves:
            new_state = state.apply_move(move)
            value, _ = alphabeta(new_state, depth - 1, alpha, beta)

            if value < best_value:
                best_value = value
                best_move = move

            beta = min(beta, value)
            if beta <= alpha:
                break  # alfa-beta ořezání

        return best_value, best_move


def find_best_move(state, depth=4):
    #Vrací nejlepší tah pro AI (frogs)
    _, move = alphabeta(state, depth, float('-inf'), float('inf'))
    return move

