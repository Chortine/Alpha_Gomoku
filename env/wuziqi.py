import tkinter as tk
from tkinter import messagebox

class GomokuGUI:
    def __init__(self, master, size=20, cell_size=15):
        self.master = master
        self.size = size
        self.cell_size = cell_size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.player_turn = 'X'
        self.master.title('Gomoku Game')

        # Create a canvas to draw the board
        self.canvas = tk.Canvas(master, height=size * cell_size, width=size * cell_size, bg="white")
        self.canvas.pack()

        # Draw the board
        for i in range(size):
            for j in range(size):
                self.canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size, outline="black")

        # Bind click event to the canvas
        self.canvas.bind("<Button-1>", self.click)

        # Display turn
        self.turn_label = tk.Label(master, text=f"Player {self.player_turn}'s turn")
        self.turn_label.pack()

    def click(self, event):
        # Calculate the click position
        x, y = event.x // self.cell_size, event.y // self.cell_size
        if self.board[y][x] == '.':
            self.board[y][x] = self.player_turn
            self.draw_piece(x, y, self.player_turn)
            if self.check_win(y, x):
                messagebox.showinfo("Game Over", f"Player {self.player_turn} wins!")
                self.reset_board()
            else:
                self.player_turn = 'O' if self.player_turn == 'X' else 'X'
                self.turn_label.config(text=f"Player {self.player_turn}'s turn")

    def draw_piece(self, x, y, player):
        # Draw a piece on the board
        piece_color = "black" if player == 'X' else "white"
        self.canvas.create_oval(x * self.cell_size + 2, y * self.cell_size + 2,
                                (x + 1) * self.cell_size - 2, (y + 1) * self.cell_size - 2,
                                fill=piece_color)

    def check_win(self, row, col):
        # Simplified win check for brevity
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for d in directions:
            if self.count_consecutive(row, col, d[0], d[1]) >= 4:
                return True
        return False

    def count_consecutive(self, row, col, d_row, d_col):
        # Count consecutive pieces for win check
        total = 0
        player = self.board[row][col]
        # Count all the pieces in the + direction
        i, j = row, col
        while 0 <= i < self.size and 0 <= j < self.size and self.board[i][j] == player:
            total += 1
            i += d_row
            j += d_col
        # Count all the pieces in the - direction
        i, j = row - d_row, col - d_col
        while 0 <= i < self.size and 0 <= j < self.size and self.board[i][j] == player:
            total += 1
            i -= d_row
            j -= d_col
        # Subtract 1 to compensate for counting the middle piece twice
        return total - 1

    def reset_board(self):
        # Reset the game board
        self.board = [['.' for _ in range(self.size)] for _ in range(self.size)]
        self.player_turn = 'X'
        self.turn_label.config(text=f"Player {self.player_turn}'s turn")
        self.canvas.delete("all")
        for i in range(self.size):
            for j in range(self.size):
                self.canvas.create_rectangle(j * self.cell_size, i * self.cell_size, (j + 1) * self.cell_size, (i + 1) * self.cell_size, outline="black")

if __name__ == "__main__":
# Create the main window
    root = tk.Tk()
    app = GomokuGUI(root)

    # Start the main loop
    root.mainloop()
