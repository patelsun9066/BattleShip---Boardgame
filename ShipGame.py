# Author: Sunny Patel
# GitHub username: patelsun9066
# Date: 2/20/2022
# Description: Battleship (Classic board game) that can be played by two players.


class ShipGame:
    """class that is responsible for the various rules and player moves for the board game: Battleship. The class
    contains methods that represents the various phases of the game. The first phase of the game is placing hidden ships
    by each respective player on their board (place_ships method), followed by players taking turns to blindly fire
    torpedoes to sink the opponents ships (fire_torpedo method), and finally the players must update the status
    of there remaining ships throughout the game (get_ships_remaining) and eventually o winner is determined
    (get_current_state method). Each method in this class will provide further details, there is only one class that is
    handling all of the program execution, it does not need to communicate with other classes.."""

    def __init__(self):
        """The ShipGame class takes no parameters, however the following private data members are initialized to
         subsequently support the various methods of the class. self._picked_positions_private_1 and
         self._picked_private_2 are initialized with empty lists to track each players picked grid positions,
         self._player_1_ship_positions and self._player_2_ship_positions are initialized to empty dictionaries to
         keep track of each respective players placed ships (grid positions, depends on length of ship). The private
         data member self._player_turn keeps track of which players turn it is when the torpedo firing begins. Finally,
         the self._current_state private data member keeps track of the game state."""

        self._picked_positions_private_1 = []  # list of all coordinates chosen by player 1
        self._picked_positions_private_2 = []  # list of all coordinate chosen by player 2
        self._player_1_ship_positions = {}  # dictionary of player 1 placed ships
        self._player_2_ship_positions = {}  # dictionary of player 2 placed ships
        self._player_turn = "first"  # The players whose turn it is to fire torpedoes
        self._current_state = "UNFINISHED"  # the current state of the game

    def place_ship(self, player, ship_length, first_position, row_or_column):
        """ The following method takes four parameters in the following order: the player placing the ship on their
        respective board (player 1 or player 2), the length of the ship being placed (has to be longer than 2, but less
        than 10), the coordinate of the first position that is closest to A1 on the 10x10 grid (essentially any letter
        from A-J, followed by any number from 1-10), and the orientation of the ship (vertical or horizontal).
        The method then attempt to place the ship on the respective players board. If the ship does not fit on the board
        ,overlaps with a previous placed ship, or if the ship length is less than 2, the method will return False
        indicating the ship was not placed. If all of these conditionals are not violated then the ship will be placed
        on the board, and the method will return True."""

        pos = first_position
        letter = pos[0]
        number = int(pos[1:])

        picked_positions = []

        if ship_length < 2:  # if ship length is less than 2, method returns false
            return False

        if player == "first":  # If player is = FIRST PLAYER
            if row_or_column == "C":  # If the ship is being placed vertical (going down) in Column
                for i in range(ship_length):
                    if pos in self._picked_positions_private_1:
                        return False  # if grid coordinate was already picked/overlaps
                    if letter > "J" or letter < "A":
                        return False  # if gird coordinate is off the 10x10 grid (vertically)
                    else:  # Coordinate is deemed valid
                        picked_positions.append(pos)  # adds coordinate to temp list
                        new_letter = chr(ord(letter) + 1)  # Letter is changed to next letter in alphabet
                        letter = new_letter
                        new_pos = str(new_letter) + str(number)  # Next coordinate - going down in vertical column
                        pos = new_pos

                if len(picked_positions) == ship_length:  # if no coordinates are overlapping/off-grid:
                    for cords in picked_positions:
                        self._picked_positions_private_1.append(cords)  # add coordinates to list.

        if player == "first":  # If player is = FIRST PLAYER
            if row_or_column == "R":  # If the ship is being placed Horizontal (going right) in row
                for i in range(ship_length):
                    if pos in self._picked_positions_private_1:
                        return False
                    if number > 10 or number < 1:
                        return False  # if grid coordinate is off the 10x10 grid (horizontally)
                    else:
                        picked_positions.append(pos)
                        new_number = number + 1  # Number is changed to number to +1
                        number = new_number
                        new_pos = str(letter) + str(
                            new_number)  # Next coordinate - going across to the left within row.
                        pos = new_pos

                if len(picked_positions) == ship_length:
                    for cords in picked_positions:
                        self._picked_positions_private_1.append(cords)

        if player == "second":  # If Player = SECOND PLAYER
            if row_or_column == "C":  # If the ship is being placed vertical (going down) in Column
                for i in range(ship_length):
                    if pos in self._picked_positions_private_2:
                        return False
                    if letter > "J" or letter < "A":
                        return False
                    else:
                        picked_positions.append(pos)
                        new_letter = chr(ord(letter) + 1)
                        letter = new_letter
                        new_pos = str(new_letter) + str(number)
                        pos = new_pos

                if len(picked_positions) == ship_length:
                    for cords in picked_positions:
                        self._picked_positions_private_2.append(cords)

        if player == "second":  # If Player = SECOND PLAYER
            if row_or_column == "R":  # If the ship is being placed Horizontal (going right) in row
                for i in range(ship_length):
                    if pos in self._picked_positions_private_2:
                        return False
                    if number > 10 or number < 1:
                        return False
                    else:
                        picked_positions.append(pos)
                        new_number = number + 1
                        number = new_number
                        new_pos = str(letter) + str(new_number)
                        pos = new_pos

                if len(picked_positions) == ship_length:
                    for cords in picked_positions:
                        self._picked_positions_private_2.append(cords)

        if player == "first":  # If Player = FIRST PLAYER
            self._player_1_ship_positions[first_position] = picked_positions  # adds ship to player 1`s board

        else:  # If Player = SECOND PLAYER
            self._player_2_ship_positions[first_position] = picked_positions  # adds ship to player 2`s board

        return True  # valid placement on player`s board

    def get_current_state(self):
        """ The following method takes no parameters, but returns the value held in the self._current_state private data
        member. The expected return value will be a string indicating the status of the game. The self._current_state is
        updated by the fire_torpedo method. The game can be updated to one of three different states: UNFINISHED
        (game is still on-going, no winner yet), SECOND_WON (second player won, all of player ones ships have been sunk)
        ,or FIRST_WON (first player won, all of player twos ships have been sunk)."""

        return self._current_state

    def fire_torpedo(self, player, target_square):
        """The following method takes two parameters: the player firing the torpedo (either player 1 or player 2, and
        the target square in the 10x10 the torpedo is fired upon. Before accepting the torpedo fire as valid, the method
        checks to see if it is the correct players turn (player 1 fires first, followed by player 2, then back
        to player 1), and checks to see if the game is still unfinished (if there is a winner game ends, no more valid
        fires). If any of these conditionals are violated, the method will return False. Otherwise, the method will
        record the fire as valid, changes the players turn, and uses the get_remaining_ships method to check if the
        valid torpedo fire resulted in the player winning (self._current_state is updated if so). Finally, the method
        will return True for a valid torpedo fire."""

        if player != self._player_turn:
            return False  # if it not the players turn
        if self._current_state != "UNFINISHED":
            return False  # if a player has already won

        if player == "second":  # if player = SECOND PLAYER
            for ships in self._player_1_ship_positions:  # On FIRST PLAYER`s board (private data member - dictionary)
                if target_square in self._player_1_ship_positions[ships]:
                    self._player_1_ship_positions[ships].remove(target_square)  # remove coordinate from list (value)
            self._player_turn = "first"  # change player turn to FIRST PLAYER
            win_check = self.get_num_ships_remaining("first")  # check FIRST PLAYER`s remaining ships
            if win_check == 0:  # if FIRST PLAYER has zero remaining ships,
                self._current_state = "SECOND_WON"  # SECOND PLAYER has won the game.

            return True  # Valid Torpedo Fire from PLAYER TWO

        if player == "first":  # if Player = FIRST PLAYER
            for ships in self._player_2_ship_positions:  # On SECOND PLAYER`s board(private data member - dictionary)
                if target_square in self._player_2_ship_positions[ships]:
                    self._player_2_ship_positions[ships].remove(target_square)  # remove coordinate from list (value)
            self._player_turn = "second"  # change player turn to SECOND PLAYER
            win_check = self.get_num_ships_remaining("second")  # check SECOND PLAYER`s remaining ships
            if win_check == 0:  # if SECOND PLAYER has zero remaining ships,
                self._current_state = "FIRST_WON"  # FIRST PLAYER has won the game

            return True  # Valid Torpedo Fire from PLAYER ONE

    def get_num_ships_remaining(self, player):
        """The following method takes one parameter: the player whose board is being checked to determine how many
        ships are still remaining (ships not sunk). The method will return the number of whole ships that are still
        remaining. Ships are considered whole if they have at least one grid coordinate that is not hit. After the
        ship placement phase of the game (via place_ship method) the method will return the total number of ships placed
        by each player.However, once the firing phase has started (fire_torpedo method) ships will be damaged upon hits.
        Once a ship has all of its grid coordinates hit by the opposing player from fire_torpedo method, the ship is
        considered to be sunk, and the remaining ships is subtracted by 1.The remaining ships will continue to decrease
        slowly until there is a winner, a player that has zero remaining ships, the method will return zero for that
        player."""

        remaining_ships_player_1 = 0
        remaining_ships_player_2 = 0

        if player == "first":   # IF player = FIRST PLAYER
            for ships in self._player_1_ship_positions:
                if len(self._player_1_ship_positions[ships]) >= 1:  # if ship has at least one un-hit coordinate
                    remaining_ships_player_1 += 1   # add +1 to respective players counter
            return remaining_ships_player_1

        if player == "second":  # IF player = SECOND PLAYER
            for ships in self._player_2_ship_positions:
                if len(self._player_2_ship_positions[ships]) >= 1:
                    remaining_ships_player_2 += 1
            return remaining_ships_player_2
