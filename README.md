# cli-based-bingo-game

Objective: The objective of the game is to be the first player to achieve a BINGO, which means marking a complete row, column, or diagonal of numbers in their respective 5x5 matrix.

Gameplay:

1. Two 5x5 matrices are created, one for the player and one for the computer (opponent), initially filled with zeros.

2. Randomly, without repetition, numbers from 1 to 25 are placed in both the player and opponent matrices.

3. The game starts, and the player and computer take turns picking numbers from 1 to 25.

4. The player enters a number, and if the number exists in both matrices, it is removed from both matrices. The player's matrix is updated accordingly.

5. The computer randomly selects a number that exists in both matrices and removes it from both matrices. The computer's matrix is updated accordingly.

6. After each turn, the game checks for BINGO conditions:
   i. A complete row or column with all numbers marked as 0.
   ii. A complete diagonal with all numbers marked as 0.

7. If a player (either the player or computer) achieves 5 BINGOs before the opponent, they win the game.

8. The game continues until one of the players wins or there are no more valid moves.

Overall, the game is a simplified version of BINGO, where the player competes against a computer opponent to mark rows, columns, or diagonals of numbers in their matrices. The first player to achieve 5 BINGOs wins the game.
