import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root, rows=6, columns=6):
        self.root = root
        self.rows = rows
        self.columns = columns
        self.buttons = []
        self.icons = [
            '😀', '😎', '😜', '😇',
            '🥳', '😻', '🙈', '🌟',
            '🍎', '🍕', '🚀', '⚽',
            '🎸', '📚', '🎲', '🎉',
            '🌈', '🏖️', '🌌', '🦄',
            '🍔', '🎮', '🍉', '🎶'
        ]
        self.matched_icons = []
        self.moves = 0
        self.opened_buttons = []  # To store currently opened buttons
        self.create_game_board()
        self.start_game()

    def create_game_board(self):
        comic_sans = ("Comic Sans MS", 14)

        for row_num in range(self.rows):
            current_row = []
            for col_num in range(self.columns):
                new_button = tk.Button(
                    self.root,
                    width=7,  # Square buttons
                    height=3,  # Square buttons
                    font=comic_sans,
                    relief="raised",
                    borderwidth=3,
                    command=lambda row=row_num, col=col_num: self.button_click(row, col)
                )
                new_button.grid(row=row_num, column=col_num, padx=5, pady=5)
                new_button.config(bg="#FAEED1", fg="black", font=comic_sans)
                current_row.append(new_button)
            self.buttons.append(current_row)

        self.root.config(bg="#FDF7E4")
        total_width = self.columns * 100  # Adjust width based on button size
        total_height = self.rows * 110  # Adjust height based on button size
        self.root.geometry(f"{total_width}x{total_height}")  # Set window size here

    def start_game(self):
        icons = self.icons * 2
        random.shuffle(icons)

        for row in range(self.rows):
            for col in range(self.columns):
                current_button = self.buttons[row][col]
                current_button.config(text="", state=tk.NORMAL)
                index = row * self.columns + col
                current_button.icon = icons[index]

    def button_click(self, row, col):
        current_button = self.buttons[row][col]

        if current_button.cget('text') == "" and len(self.opened_buttons) < 2:
            current_button.config(text=current_button.icon)
            self.opened_buttons.append(current_button)

            if len(self.opened_buttons) == 2:
                self.root.after(1000, self.check_match)

    def check_match(self):
        if self.opened_buttons[0].cget('text') == self.opened_buttons[1].cget('text'):
            for button in self.opened_buttons:
                button.config(state=tk.DISABLED)
        else:
            for button in self.opened_buttons:
                button.config(text="")

        self.opened_buttons = []
        self.moves += 1
        if self.check_win():
            tk.messagebox.showinfo("Congratulations!", f"You won in {self.moves} moves!")
            self.restart_game()

    def check_win(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.buttons[row][col]['state'] != tk.DISABLED:
                    return False
        return True

    def restart_game(self):
        self.moves = 0
        self.opened_buttons = []
        self.start_game()

def main():
    root = tk.Tk()
    root.title("Memory Game")
    memory_game = MemoryGame(root, rows=6, columns=6)
    root.mainloop()

if __name__ == "__main__":
    main()
