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
        self.create_game_board()
        self.start_game()

    def create_game_board(self):
        comic_sans = ("Comic Sans MS", 14)

        for row_num in range(self.rows):
            current_row = []
            for col_num in range(self.columns):
                new_button = tk.Button(
                    self.root,
                    width=8,
                    height=4,
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
        self.root.geometry("660x820")  # Set window size here

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

        if current_button.cget('text') == "":
            current_button.config(text=current_button.icon)
            self.matched_icons.append(current_button)

        if len(self.matched_icons) == 2:
            self.root.after(1000, self.check_match)

    def check_match(self):
        if self.matched_icons[0].cget('text') == self.matched_icons[1].cget('text'):
            for button in self.matched_icons:
                button.config(state=tk.DISABLED)
        else:
            for button in self.matched_icons:
                button.config(text="")

        self.matched_icons = []
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
        self.matched_icons = []
        self.start_game()

def main():
    root = tk.Tk()
    root.title("Memory Game")
    memory_game = MemoryGame(root, rows=6, columns=6)
    root.mainloop()

if __name__ == "__main__":
    main()
