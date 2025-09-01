#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Vérifie les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifie les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifie la diagonale principale
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Vérifie la diagonale secondaire
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def is_full(board):
    """Retourne True si le tableau est plein (match nul)."""
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Demande de coordonnées avec gestion des erreurs
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Invalid input! Please enter numbers 0, 1, or 2.")
            continue

        # Vérifie si la position est valide
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid position! Try again.")
            continue

        # Vérifie si la case est libre
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place le symbole du joueur
        board[row][col] = player

        # Vérifie si ce joueur gagne
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        # Vérifie le match nul
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Change de joueur
        player = "O" if player == "X" else "X"


tic_tac_toe()