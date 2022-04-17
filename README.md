# BattleShip---Boardgame 
Battleship (Classic board game) that can be played by two players. The rules of the game of are simple! Each player has their own 10x10 grid they place their ships on. On their turn, they can fire a torpedo at a square on the enemy's grid. Player 'first' gets the first turn to fire a torpedo, after which players alternate firing torpedos. A ship is sunk when all of its squares have been hit. When a player sinks their opponent's final ship, they win.

Thus far only the back-end of this game has been developed using Python (GUI/Visual front-end is a work-in-progress!) , however with the right functions calls this game can be fully played out! Please see a summarization below of which classes, and corresponding methods control the operations of each phase and action of this game. 

ShipClass (class) - has no parameters and sets all data members to their initial values. The data members represent each player`s 10x10 grid.

  place_ship (method) - takes as parameters: the player (either 'first' or 'second' as string), the length of the ship (integer) , the coordinates of the square it will   occupy that is closest to A1 (String) , and the ship's orientation - either 'R' if its squares occupy the same row, or 'C' if its squares occupy the same column         (String). If a ship would not fit entirely on that player's grid, or if it would overlap any previously placed ships on that player's grid, or if the length of the       ship is less than 2, the ship wil not be added and the method will return False. Otherwise, the ship will be added and the method will return True.
  
  get_current_state (method) - takes no parameters. Returns the current state of the game: either 'FIRST_WON', 'SECOND_WON', or 'UNFINISHED'.
  
  fire_torpedo (method) - takes as arguments the player firing the torpedo (either 'first' or 'second' as String) and the coordinates of the target square, e.g. 'B7'       (String). If it's not that player's turn, or if the game has already been won, the method will return False. Otherwise, it will record the move, update whose turn it     is next, update the current state (if this turn sank the opponent's final ship), and will return True.
  
  get_num_ships_remaining (method) -  takes as an argument either "first" or "second" (String) and returns how many ships the specified player has left.
  
Happy Playing! Hope you enjoy this classic board game!

