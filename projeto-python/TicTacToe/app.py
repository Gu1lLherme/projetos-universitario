from tkinter import *
co0 = "#FFFFFF"  # branca 
co1 = "#333333"  # preta pesado
co2 = "#fcc058"  # laranja 
co3 = "#38576b"  # valor 
co4 = "#3297a8"   # azul 
co5 = "#fff873"   # amarela 
co6 = "#fcc058"  # laranja 
co7 = "#e85151"   # vermelha 
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta 

# Other color definitions
...

# Create Tic Tac Toe board
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.root.geometry('400x550')
        self.root.configure(bg=fundo)
        self.root.resizable(width=False, height=False)

        # Define players and scores
        self.players = ['X', 'O']
        self.scores = [0, 0]
        self.current_player = 0

        # Create frame for score
        self.frame_superior = Frame(root, width=380, height=150, bg=co1, relief="raised")
        self.frame_superior.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

        # Create frame for game board
        self.frame_inferior = Frame(root, width=380, height=400, bg=fundo, relief="flat")
        self.frame_inferior.grid(row=1, column=0, sticky=NW, padx=10)

        # Initialize Tic Tac Toe board
        self.create_board()

    def create_board(self):
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = Button(self.frame_inferior, command=lambda row=i, col=j: self.handle_click(row, col),
                                text="", height=1, width=4, pady=5, font=('Ivy 30 bold'),
                                overrelief=RIDGE, relief='flat', bg=fundo)
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)

    def handle_click(self, row, col):
        button_index = row * 3 + col
        button = self.buttons[button_index]

        if button['text'] == "":
            button['text'] = self.players[self.current_player]

            # Check for winner
            if self.check_winner():
                winner = self.players[self.current_player]
                print(f"Player {winner} wins!")
                self.scores[self.current_player] += 1
                self.update_scores()
                self.reset_board()
            else:
                self.current_player = (self.current_player + 1) % 2

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        # Return True if a player has won, False otherwise
        # Implement your logic here
        pass

    def update_scores(self):
        # Update the scores displayed on the GUI
        # Implement your logic here
        pass

    def reset_board(self):
        # Reset the game board to start a new game
        for button in self.buttons:
            button['text'] = ""


def main():
    janela = Tk()
    game = TicTacToe(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()