from game_state import GameState, Move
from ai import find_best_move, evaluate

print("== TEST 1: generate_moves ==")
state = GameState(['T', '.', 'F', '.'], current_player='T')
moves = state.generate_moves()
print("Board:", state.board)
print("Moves:", [(m.from_idx, m.to_idx) for m in moves])
#použiju ten jediny move
for m in moves:
    new_state = state.apply_move(m)
    print("Applied move:", new_state.board)
print()


print("== TEST 2: apply_move ==")
state = GameState(['T', '.', 'F', '.'], current_player='T')
move = Move(0, 1)
new_state = state.apply_move(move)
print("Original board:", state.board)
print("New board:", new_state.board)
print()


print("== TEST 3: clone ==")
state = GameState(['T', '.', 'F'], current_player='T')
clone = state.clone()
clone.board[0] = '.'
print("Original board:", state.board)
print("Clone board:", clone.board)
print()


print("== TEST 4: evaluate ==")
state1 = GameState(['.', 'F', '.', 'T'], current_player='F')
state2 = GameState(['.', 'T', '.', 'F'], current_player='F')
val1 = evaluate(state1)
val2 = evaluate(state2)
print("Board1:", state1.board)
print("Evaluate1:", val1)
print("Board2:", state2.board)
print("Evaluate2:", val2)
print()


print("== TEST 5: find_best_move() ==")
state = GameState(['.', 'F', 'F', 'T', 'T'], current_player = 'F')
move = find_best_move(state)
print(move)
print()


print("== TEST 6: AI depth = 1 ==")
state = GameState(['T', '.', 'F'], current_player='F')
best_move = find_best_move(state, depth=1)
print("Board:", state.board)
print("AI best move:", (best_move.from_idx, best_move.to_idx))
print()


print("== TEST 7: More moves ==")
state = GameState(['.', 'T', '.', 'T', 'F', '.'])
moves = state.generate_moves()
print("Board:", state.board)
print("Moves:", [(m.from_idx, m.to_idx) for m in moves])
for m in moves:
    new_state = state.apply_move(m)
    print("Applied move:", new_state.board)
print()


print("== TEST 8: is_terminal() ==")
state1 = GameState(['.', 'F', 'F', 'T', 'T'], )
state2 = GameState(['T', 'F', 'F', 'T', '.'])
print(state1.is_terminal())
print(state2.is_terminal())
print()
