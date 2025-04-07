import tkinter as tk
from tkinter import messagebox


class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]

        # Create buttons for the game board
        self.buttons = []
        for i in range(9):
            button = tk.Button(
                root,
                text=" ",
                font=('Helvetica', 20),
                height=3,
                width=6,
                bg='lightblue',
                command=lambda idx=i: self.on_button_click(idx)
            )
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        # Add reset button
        reset_button = tk.Button(
            root,
            text="Reset Game",
            font=('Helvetica', 12),
            bg='lightgreen',
            command=self.reset_game
        )
        reset_button.grid(row=3, column=0, columnspan=3, sticky="we")

    def on_button_click(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] != " " and self.board[a] == self.board[b] == self.board[c]:
                # Highlight winning combination
                self.buttons[a].config(bg='lightgreen')
                self.buttons[b].config(bg='lightgreen')
                self.buttons[c].config(bg='lightgreen')
                return True
        return False

    def reset_game(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ", bg='lightblue')


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()