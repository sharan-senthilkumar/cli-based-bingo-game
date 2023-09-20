import tkinter as tk
import random

def initialize_matrices():
    player_matrix = [[0] * 5 for _ in range(5)]
    opponent_matrix = [[0] * 5 for _ in range(5)]
    numbers = list(range(1, 26))
    
    for matrix in [player_matrix, opponent_matrix]:
        for _ in range(25):
            if not numbers:
                break
            row, col = random.randint(0, 4), random.randint(0, 4)
            while matrix[row][col] != 0:
                row, col = random.randint(0, 4), random.randint(0, 4)
            matrix[row][col] = numbers.pop(0)
    
    return player_matrix, opponent_matrix

def is_winner(bingo_count):
    return bingo_count >= 5

def check_bingo(matrix):
    bingo_count = 0
    for i in range(5):
        if all(matrix[i][j] == 0 for j in range(5)):  # Check rows
            bingo_count += 1
        if all(matrix[j][i] == 0 for j in range(5)):  # Check columns
            bingo_count += 1
    # Check diagonals
    if all(matrix[i][i] == 0 for i in range(5)) or all(matrix[i][4 - i] == 0 for i in range(5)):
        bingo_count += 1
    return bingo_count

def on_button_click(number):
    global player_matrix, opponent_matrix, player_bingo_count, opponent_bingo_count
    
    if not (number in selected_numbers or number in opponent_numbers):
        selected_numbers.add(number)
        button = buttons[number - 1]
        button["state"] = "disabled"
        button["bg"] = "gray"
        
        if number in [player_matrix[i][j] for i in range(5) for j in range(5)]:
            player_bingo_count = check_bingo(player_matrix)
            label_player_bingo_count.config(text=f"Player's BINGO Count: {player_bingo_count}")
            if is_winner(player_bingo_count):
                label_result.config(text="Congratulations! You win!")
                disable_buttons()
                return
        
        opponent_pick = random.choice(opponent_numbers)
        opponent_numbers.remove(opponent_pick)
        if opponent_pick in [opponent_matrix[i][j] for i in range(5) for j in range(5)]:
            opponent_bingo_count = check_bingo(opponent_matrix)
            label_opponent_bingo_count.config(text=f"Opponent's BINGO Count: {opponent_bingo_count}")
            if is_winner(opponent_bingo_count):
                label_result.config(text="Opponent wins!")
                disable_buttons()
                return

def disable_buttons():
    for button in buttons:
        button["state"] = "disabled"

root = tk.Tk()
root.title("BINGO Game")

player_matrix, opponent_matrix = initialize_matrices()
selected_numbers = set()
opponent_numbers = set(range(1, 26))
player_bingo_count = 0
opponent_bingo_count = 0

label_player_bingo_count = tk.Label(root, text="Player's BINGO Count: 0")
label_player_bingo_count.grid(row=0, column=0, columnspan=5)

label_opponent_bingo_count = tk.Label(root, text="Opponent's BINGO Count: 0")
label_opponent_bingo_count.grid(row=1, column=0, columnspan=5)

label_result = tk.Label(root, text="")
label_result.grid(row=2, column=0, columnspan=5)

buttons = []
for i in range(1, 26):
    button = tk.Button(root, text=str(i), width=5, height=2, command=lambda i=i: on_button_click(i))
    buttons.append(button)
    row, col = (i - 1) // 5 + 3, (i - 1) % 5
    button.grid(row=row, column=col)

root.mainloop()
