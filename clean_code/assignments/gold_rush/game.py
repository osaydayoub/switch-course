from Matrix import Matrix
import random


class GoldRush(Matrix):
    WINNING_SCORE = 100
    COIN = "$"
    WALL = "wall"
    EMPTY_SPACE = "."
    FIRST_PLAYER = "player1"
    SECOND_PLAYER = "player2"
    MIN_COINS = 10


    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.player1_score = 0
        self.player2_score = 0
        self.winner = ""
        self.coins = 0
    
    def _is_zero_sized_board(self):
        return self.rows == 0 and self.cols == 0
    
    def _init_board(self):
        self.matrix = []
        for _ in range(self.rows):
            self.matrix.append([])
    
    def _fill_row(self,row_number,elements):
        coins = 0
        for j in range(self.cols):
            if row_number % 2 != 0:
                rand_index = random.randint(0, 1)  
                rand_element = elements[rand_index]
                self.matrix[row_number].append(rand_element)

                if rand_element == GoldRush.COIN:
                    coins += 1
            else:
                self.matrix[row_number].append(GoldRush.WALL)
        return coins
    
    def _randomize_row(self,row_number,elements):
        coins = 0
        rand = random.randint(1, 2)
        for k in range(1, self.cols, rand):
            rand += 1
            rand_index = random.randint(0, 1)
            rand_element = elements[rand_index]
            self.matrix[row_number][k] = rand_element

            if rand_element == GoldRush.COIN:
                coins += 1
        return coins

    def _populate_board(self):
        elements = [GoldRush.COIN, GoldRush.EMPTY_SPACE, GoldRush.WALL]
        coins = 0
        for i in range(self.rows):
            coins += self._fill_row(i,elements)
            coins += self._randomize_row(i,elements)
        return coins
    
    def _place_players(self):
        self.matrix[0][0] = GoldRush.FIRST_PLAYER
        self.matrix[self.rows - 1][self.cols - 1] = GoldRush.SECOND_PLAYER

    def load_board(self):
        if self._is_zero_sized_board():
            self.matrix = []
            return
        self._init_board()
        coins = self._populate_board()
        self._place_players()
        self.coins = coins  
        if coins < GoldRush.MIN_COINS:
            return self.load_board()
        else:
            return self.matrix


    def _check_winner(self, player):
        player_num = player[-1]
        score = getattr(self, f"player{player_num}_score")
        if score == GoldRush.WINNING_SCORE:
            self.winner = player
            return self.winner

    def _check_other_player(self, player):
        otherPlayer = None
        if player == GoldRush.FIRST_PLAYER:
            otherPlayer = GoldRush.SECOND_PLAYER
            return otherPlayer
        elif player == GoldRush.SECOND_PLAYER:
            otherPlayer = GoldRush.FIRST_PLAYER
            return otherPlayer
        

    def _move(self, curr_row, curr_col, player, delta_row, delta_col):
        other_player = self._check_other_player(player)
        new_row, new_col = curr_row + delta_row, curr_col + delta_col

        if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
            return

        if self.matrix[new_row][new_col] not in [GoldRush.WALL, other_player]:
            if self.matrix[new_row][new_col] == GoldRush.COIN:
                self._increase_score(player)

            self.matrix[curr_row][curr_col] = GoldRush.EMPTY_SPACE
            self.matrix[new_row][new_col] = player

        return self._check_winner(player)

    def _move_down(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 1, 0)

    def _move_up(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, -1, 0)

    def _move_right(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 0, 1)

    def _move_left(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 0, -1)

    def move_player(self, player, direction):
        curr_row, curr_col = None, None

        for i, row in enumerate(self.matrix):
            for j, value in enumerate(row):
                if value == player:
                    curr_row, curr_col = i, j
                    break
            if curr_row is not None:
                break

        if direction == "down":
            self._move_down(curr_row, curr_col, player)
        elif direction == "up":
            self._move_up(curr_row, curr_col, player)
        elif direction == "right":
            self._move_right(curr_row, curr_col, player)
        elif direction == "left":
            self._move_left(curr_row, curr_col, player)

    def _increase_score(self, player):
        player_num = player[-1]
        score_attr = f"player{player_num}_score"
        setattr(self, score_attr, getattr(self, score_attr) + 10)
        print(getattr(self, score_attr))
