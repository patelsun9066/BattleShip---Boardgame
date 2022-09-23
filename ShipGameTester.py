import unittest
from ShipGame import ShipGame


class TestShipGame(unittest.TestCase):

    def test_1(self):
        """Fill every position on Board for Player 1. Not testing overlap or off the board moves.  """

        game = ShipGame()
        place_ship_1 = game.place_ship('first', 5, 'A1', 'C')
        self.assertTrue(place_ship_1)
        place_ship_2 = game.place_ship('first', 9, 'A2', 'R')
        self.assertTrue(place_ship_2)
        place_ship_3 = game.place_ship('first', 9, 'B10', 'C')
        self.assertTrue(place_ship_3)
        place_ship_4 = game.place_ship('first', 9, 'J1', 'R')
        self.assertTrue(place_ship_4)
        place_ship_5 = game.place_ship('first', 9, 'I1', 'R')
        self.assertTrue(place_ship_5)
        place_ship_6 = game.place_ship('first', 9, 'H1', 'R')
        self.assertTrue(place_ship_6)
        place_ship_7 = game.place_ship('first', 9, 'G1', 'R')
        self.assertTrue(place_ship_7)
        place_ship_8 = game.place_ship('first', 9, 'F1', 'R')
        self.assertTrue(place_ship_8)
        place_ship_9 = game.place_ship('first', 4, 'B2', 'C')
        self.assertTrue(place_ship_9)
        place_ship_10 = game.place_ship('first', 4, 'B3', 'C')
        self.assertTrue(place_ship_10)
        place_ship_11 = game.place_ship('first', 4, 'B4', 'C')
        self.assertTrue(place_ship_11)
        place_ship_12 = game.place_ship('first', 4, 'B5', 'C')
        self.assertTrue(place_ship_12)
        place_ship_13 = game.place_ship('first', 4, 'B6', 'C')
        self.assertTrue(place_ship_13)
        place_ship_14 = game.place_ship('first', 4, 'B7', 'C')
        self.assertTrue(place_ship_14)
        place_ship_15 = game.place_ship('first', 4, 'B8', 'C')
        self.assertTrue(place_ship_15)
        place_ship_16 = game.place_ship('first', 4, 'B9', 'C')
        self.assertTrue(place_ship_16)

    def test_2(self):
        """Fill every position on Board for Player 2. Not testing overlap or off the board moves.  """
        game = ShipGame()
        place_ship_1 = game.place_ship('second', 5, 'A1', 'C')
        self.assertTrue(place_ship_1)
        place_ship_2 = game.place_ship('second', 9, 'A2', 'R')
        self.assertTrue(place_ship_2)
        place_ship_3 = game.place_ship('second', 9, 'B10', 'C')
        self.assertTrue(place_ship_3)
        place_ship_4 = game.place_ship('second', 9, 'J1', 'R')
        self.assertTrue(place_ship_4)
        place_ship_5 = game.place_ship('second', 9, 'I1', 'R')
        self.assertTrue(place_ship_5)
        place_ship_6 = game.place_ship('second', 9, 'H1', 'R')
        self.assertTrue(place_ship_6)
        place_ship_7 = game.place_ship('second', 9, 'G1', 'R')
        self.assertTrue(place_ship_7)
        place_ship_8 = game.place_ship('second', 9, 'F1', 'R')
        self.assertTrue(place_ship_8)
        place_ship_9 = game.place_ship('second', 4, 'B2', 'C')
        self.assertTrue(place_ship_9)
        place_ship_10 = game.place_ship('second', 4, 'B3', 'C')
        self.assertTrue(place_ship_10)
        place_ship_11 = game.place_ship('second', 4, 'B4', 'C')
        self.assertTrue(place_ship_11)
        place_ship_12 = game.place_ship('second', 4, 'B5', 'C')
        self.assertTrue(place_ship_12)
        place_ship_13 = game.place_ship('second', 4, 'B6', 'C')
        self.assertTrue(place_ship_13)
        place_ship_14 = game.place_ship('second', 4, 'B7', 'C')
        self.assertTrue(place_ship_14)
        place_ship_15 = game.place_ship('second', 4, 'B8', 'C')
        self.assertTrue(place_ship_15)
        place_ship_16 = game.place_ship('second', 4, 'B9', 'C')
        self.assertTrue(place_ship_16)

    def test_3(self):
        """Player 1 Board - Testing Overlap and Off - Grid positions  """

        game = ShipGame()
        place_ship_1 = game.place_ship('first', 4, 'H1', 'C')
        self.assertFalse(place_ship_1)
        place_ship_2 = game.place_ship('first', 4, 'H1', 'R')
        self.assertTrue(place_ship_2)
        place_ship_3 = game.place_ship('first', 5, 'E3', 'C')
        self.assertFalse(place_ship_3)
        place_ship_4 = game.place_ship('first', 3, 'D9', 'R')
        self.assertFalse(place_ship_4)
        place_ship_5 = game.place_ship('first', 3, 'C9', 'C')
        self.assertTrue(place_ship_5)
        place_ship_6 = game.place_ship('first', 4, 'E7', 'R')
        self.assertFalse(place_ship_6)
        place_ship_7 = game.place_ship('first', 1, 'J4', 'R')
        self.assertFalse(place_ship_7)
        place_ship_8 = game.place_ship('first', 2, 'I4', 'C')
        self.assertTrue(place_ship_8)
        place_ship_9 = game.place_ship('first', 3, 'J8', 'R')
        self.assertTrue(place_ship_9)
        place_ship_10 = game.place_ship('first', 5, 'I7', 'R')
        self.assertFalse(place_ship_10)
        place_ship_11 = game.place_ship('first', 11, 'A5', 'C')
        self.assertFalse(place_ship_11)
        place_ship_12 = game.place_ship('first', 6, 'B1', 'R')
        self.assertTrue(place_ship_12)
        place_ship_13 = game.place_ship('first', 5, 'B6', 'R')
        self.assertFalse(place_ship_13)

    def test_4(self):
        """Player 2 Board - Testing Overlap and Off - Grid positions  """

        game = ShipGame()
        place_ship_1 = game.place_ship('second', 4, 'H1', 'C')
        self.assertFalse(place_ship_1)
        place_ship_2 = game.place_ship('second', 4, 'H1', 'R')
        self.assertTrue(place_ship_2)
        place_ship_3 = game.place_ship('second', 5, 'E3', 'C')
        self.assertFalse(place_ship_3)
        place_ship_4 = game.place_ship('second', 3, 'D9', 'R')
        self.assertFalse(place_ship_4)
        place_ship_5 = game.place_ship('second', 3, 'C9', 'C')
        self.assertTrue(place_ship_5)
        place_ship_6 = game.place_ship('second', 4, 'E7', 'R')
        self.assertFalse(place_ship_6)
        place_ship_7 = game.place_ship('second', 1, 'J4', 'R')
        self.assertFalse(place_ship_7)
        place_ship_8 = game.place_ship('second', 2, 'I4', 'C')
        self.assertTrue(place_ship_8)
        place_ship_9 = game.place_ship('second', 3, 'J8', 'R')
        self.assertTrue(place_ship_9)
        place_ship_10 = game.place_ship('second', 5, 'I7', 'R')
        self.assertFalse(place_ship_10)
        place_ship_11 = game.place_ship('second', 11, 'A5', 'C')
        self.assertFalse(place_ship_11)
        place_ship_12 = game.place_ship('second', 6, 'B1', 'R')
        self.assertTrue(place_ship_12)
        place_ship_13 = game.place_ship('second', 5, 'B6', 'R')
        self.assertFalse(place_ship_13)

    def test_5(self):
        """README SAMPLE EXAMPLE USE """

        game = ShipGame()
        game.place_ship('first', 5, 'B2', 'C')
        game.place_ship('first', 2, 'I8', 'R')
        game.place_ship('second', 3, 'H2', 'C')
        game.place_ship('second', 2, 'A1', 'C')
        game.place_ship('first', 8, 'H2', 'R')
        game.fire_torpedo('first', 'H3')
        game.fire_torpedo('second', 'A1')
        answer = game.get_current_state()
        self.assertEqual(answer, "UNFINISHED")

    def test_6(self):
        """Game stimulation. Place ship - No enforcement of taking turns for players. no overlap or off grid test
        Torpedo - Test that taking turns is working. Test both hits, misses, and fire on already hit spots and
         missed sports. Test out of player turn is false. Test move after a player wins is false.
          remaining ships method - test throughout game. test when one player wins the other - should be zero.
          test to make sure partially hit ships are not -1. Ships fully hit are -1.
          Current State - test to see if player two can win."""
        game = ShipGame()
        game.place_ship('first', 5, 'A1', 'R')
        game.place_ship('second', 5, 'C2', 'C')
        game.place_ship('first', 4, 'B7', 'C')
        game.place_ship('second', 3, 'H4', 'C')
        game.place_ship('first', 2, 'H10', 'C')
        game.place_ship('first', 3, 'G2', 'R')
        game.place_ship('first', 4, 'J4', 'R')
        game.place_ship('second', 5, 'G3', 'R')
        game.place_ship('second', 2, 'B7', 'C')
        game.place_ship('second', 4, 'C10', 'C')
        # PLayer 1 - 5 ships ,   PLayer 2 - 5 ships
        ships_check = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check, 5)
        ships_check_2 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_2, 5)

        Out_of_turn_test = game.fire_torpedo('second', 'H3')  # OUT OF PLAYER TURN TEST
        self.assertFalse(Out_of_turn_test)
        fire_1 = game.fire_torpedo('first', 'A1')  # missed fire, should still be True
        self.assertTrue(fire_1)
        fire_2 = game.fire_torpedo('second', 'A1')  # HIT
        self.assertTrue(fire_2)
        fire_3 = game.fire_torpedo('first', 'A1')  # missed fire on same spot missed fired before, should be TRUE
        self.assertTrue(fire_3)
        fire_4 = game.fire_torpedo('second', 'A1')  # fire on same spot hit before, Should be True
        self.assertTrue(fire_4)
        fire_5 = game.fire_torpedo('first', 'B7')  # HIT - TRUE
        self.assertTrue(fire_5)
        fire_6 = game.fire_torpedo('second', 'C2')  # MISS - True
        self.assertTrue(fire_6)
        fire_7 = game.fire_torpedo('first', 'B7')  # FIRE ON previous hit spot - True
        self.assertTrue(fire_7)
        ships_check = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check, 5)
        ships_check_2 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_2, 5)
        fire_8 = game.fire_torpedo('second', 'C2')  # RE-Fired on previous missed spot - True
        self.assertTrue(fire_8)
        answer = game.get_current_state()
        self.assertEqual(answer, "UNFINISHED")  # Game not finished
        game.fire_torpedo('first', 'C7')
        ships_check = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check, 4)
        ships_check_2 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_2, 5)
        game.fire_torpedo('second', 'A2')
        game.fire_torpedo('first', 'C2')
        game.fire_torpedo('second', 'A3')
        game.fire_torpedo('first', 'D2')
        game.fire_torpedo('second', 'A4')
        game.fire_torpedo('first', 'E2')
        game.fire_torpedo('second', 'A5')
        ships_check_3 = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_3, 4)
        ships_check_4 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_4, 4)

        game.fire_torpedo('first', 'F2')
        game.fire_torpedo('second', 'B7')
        game.fire_torpedo('first', 'G2')  # player 1 sunk another player 2 ship
        game.fire_torpedo('second', 'C7')
        game.fire_torpedo('first', 'G3')
        game.fire_torpedo('second', 'D7')

        game.fire_torpedo('first', 'G4')
        game.fire_torpedo('second', 'E7')  # player 2 sunk another player 1 ship
        game.fire_torpedo('first', 'G5')
        game.fire_torpedo('second', 'H10')
        game.fire_torpedo('first', 'G6')
        game.fire_torpedo('second', 'I10')  # player 2 sunk another ship
        game.fire_torpedo('first', 'G7')  # player 1 sunk another ship

        ships_check_5 = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_5, 2)
        ships_check_6 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_6, 2)

        game.fire_torpedo('second', 'G2')
        game.fire_torpedo('first', 'H4')
        game.fire_torpedo('second', 'G3')
        game.fire_torpedo('first', 'I4')
        game.fire_torpedo('second', 'G4')  # player 2 sunk another ship
        game.fire_torpedo('first', 'J4')  # player 1 sunk another ship

        ships_check_5 = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_5, 1)
        ships_check_6 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_6, 1)

        game.fire_torpedo('second', 'J4')
        game.fire_torpedo('first', 'C10')
        game.fire_torpedo('second', 'J5')
        game.fire_torpedo('first', 'D10')
        game.fire_torpedo('second', 'J6')
        game.fire_torpedo('first', 'E10')
        game.fire_torpedo('second', 'J7')  # SECOND PLAYER WON game
        game_over_move = game.fire_torpedo('first', 'F10')  # GAME OVER - FALSE MOVE

        # ending checks
        self.assertFalse(game_over_move)
        answer = game.get_current_state()
        self.assertEqual(answer, "SECOND_WON")  # Game not finished
        ships_check_final_second = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_final_second, 1)
        ships_check_final_first = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_final_first, 0)

    def test_7(self):
        """Same tests as Test 6, but checking to see if player 1 can win."""
        game = ShipGame()
        game.place_ship('first', 5, 'A1', 'R')
        game.place_ship('second', 5, 'C2', 'C')
        game.place_ship('first', 4, 'B7', 'C')
        game.place_ship('second', 3, 'H4', 'C')
        game.place_ship('first', 2, 'H10', 'C')
        game.place_ship('first', 3, 'G2', 'R')
        game.place_ship('first', 4, 'J4', 'R')
        game.place_ship('second', 5, 'G3', 'R')
        game.place_ship('second', 2, 'B7', 'C')
        game.place_ship('second', 4, 'C10', 'C')
        # PLayer 1 - 5 ships ,   PLayer 2 - 5 ships
        ships_check = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check, 5)
        ships_check_2 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_2, 5)

        Out_of_turn_test = game.fire_torpedo('second', 'H3')  # OUT OF PLAYER TURN TEST
        self.assertFalse(Out_of_turn_test)
        fire_1 = game.fire_torpedo('first', 'A1')  # missed fire, should still be True
        self.assertTrue(fire_1)
        fire_2 = game.fire_torpedo('second', 'A1')  # HIT
        self.assertTrue(fire_2)
        fire_3 = game.fire_torpedo('first', 'A1')  # missed fire on same spot missed fired before, should be TRUE
        self.assertTrue(fire_3)
        fire_4 = game.fire_torpedo('second', 'A1')  # fire on same spot hit before, Should be True
        self.assertTrue(fire_4)
        fire_5 = game.fire_torpedo('first', 'B7')  # HIT - TRUE
        self.assertTrue(fire_5)
        fire_6 = game.fire_torpedo('second', 'C2')  # MISS - True
        self.assertTrue(fire_6)
        fire_7 = game.fire_torpedo('first', 'B7')  # FIRE ON previous hit spot - True
        self.assertTrue(fire_7)
        fire_8 = game.fire_torpedo('second', 'C2')  # RE-Fired on previous missed spot - True
        self.assertTrue(fire_8)
        answer = game.get_current_state()
        self.assertEqual(answer, "UNFINISHED")  # Game not finished
        game.fire_torpedo('first', 'C7')
        ships_check = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check, 4)
        ships_check_2 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_2, 5)
        game.fire_torpedo('second', 'A2')
        game.fire_torpedo('first', 'C2')
        game.fire_torpedo('second', 'A3')
        game.fire_torpedo('first', 'D2')
        game.fire_torpedo('second', 'A4')
        game.fire_torpedo('first', 'E2')
        game.fire_torpedo('second', 'A5')
        ships_check_3 = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_3, 4)
        ships_check_4 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_4, 4)

        game.fire_torpedo('first', 'F2')
        game.fire_torpedo('second', 'B7')
        game.fire_torpedo('first', 'G2')  # player 1 sunk another player 2 ship
        game.fire_torpedo('second', 'C7')
        game.fire_torpedo('first', 'G3')
        game.fire_torpedo('second', 'D7')

        game.fire_torpedo('first', 'G4')
        game.fire_torpedo('second', 'E7')  # player 2 sunk another player 1 ship
        game.fire_torpedo('first', 'G5')
        game.fire_torpedo('second', 'H10')
        game.fire_torpedo('first', 'G6')
        game.fire_torpedo('second', 'I10')  # player 2 sunk another ship
        game.fire_torpedo('first', 'G7')  # player 1 sunk another ship

        ships_check_5 = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_5, 2)
        ships_check_6 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_6, 2)
        answer = game.get_current_state()
        self.assertEqual(answer, "UNFINISHED")  # Game not finished

        game.fire_torpedo('second', 'G2')
        game.fire_torpedo('first', 'H4')
        game.fire_torpedo('second', 'G3')
        game.fire_torpedo('first', 'I4')
        game.fire_torpedo('second', 'G4')  # player 2 sunk another ship
        game.fire_torpedo('first', 'J4')  # player 1 sunk another ship

        ships_check_5 = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_5, 1)
        ships_check_6 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_6, 1)

        game.fire_torpedo('second', 'J4')
        game.fire_torpedo('first', 'C10')
        game.fire_torpedo('second', 'J5')
        game.fire_torpedo('first', 'D10')
        game.fire_torpedo('second', 'J6')
        game.fire_torpedo('first', 'E10')
        game.fire_torpedo('second', 'J6')  # SECOND PLAYER MISSES THE GAME WINNER
        game_over_move = game.fire_torpedo('first', 'F10')  # PLAYER ONE WINS
        false_move_1 = game.fire_torpedo('second', 'J7')  # FALSE MOVE
        false_move_2 = game.fire_torpedo('first', 'E10')  # FALSE MOVE

        # ending checks
        self.assertTrue(game_over_move)
        self.assertFalse(false_move_1)
        self.assertFalse(false_move_2)
        answer = game.get_current_state()
        self.assertEqual(answer, "FIRST_WON")  # Game finished
        ships_check_final_second = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_final_second, 0)
        ships_check_final_first = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_final_first, 1)

    def test_8(self):
        """Comprehensive Test."""
        # Placing ship phase
        game = ShipGame()
        game.place_ship('first', 5, 'A10', 'R')
        ships_check_no_add = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_no_add, 0)
        game.place_ship('first', 5, 'A1', 'R')
        game.place_ship('first', 2, 'A10', 'R')  # off the grid - horizontal test
        game.place_ship('first', 4, 'H3', 'C')  # off the grid - vertical test
        game.place_ship('second', 5, 'C2', 'C')
        game.place_ship('second', 5, 'C1', 'R')  # test overlap - horizontal
        game.place_ship('second', 5, 'C7', 'R')  # off the grid - horizontal test
        game.place_ship('second', 3, 'I9', 'C')  # off the grid - vertical test
        game.place_ship('first', 4, 'B7', 'C')
        game.place_ship('first', 4, 'B6', 'R')  # test overlap - horizontal
        game.place_ship('second', 3, 'H4', 'C')
        game.place_ship('first', 2, 'H10', 'C')
        game.place_ship('first', 3, 'G2', 'R')
        game.place_ship('first', 3, 'F2', 'C')  # test overlap - vertical
        game.place_ship('first', 4, 'J4', 'R')
        game.place_ship('second', 5, 'G3', 'R')
        game.place_ship('second', 3, 'F7', 'C')  # test overlap - vertical
        game.place_ship('second', 2, 'B7', 'C')
        game.place_ship('second', 4, 'C10', 'C')
        # PLayer 1 - 5 ships ,   PLayer 2 - 5 ships
        ships_check = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check, 5)
        ships_check_2 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_2, 5)
        answer = game.get_current_state()
        self.assertEqual(answer, "UNFINISHED")  # Game not finished

        # Fire phase begins below

        Out_of_turn_test = game.fire_torpedo('second', 'H3')  # OUT OF PLAYER TURN TEST
        self.assertFalse(Out_of_turn_test)
        fire_1 = game.fire_torpedo('first', 'A1')  # missed fire, should still be True
        self.assertTrue(fire_1)
        fire_2 = game.fire_torpedo('second', 'A1')  # HIT
        self.assertTrue(fire_2)
        fire_3 = game.fire_torpedo('first', 'A1')  # missed fire on same spot missed fired before, should be TRUE
        self.assertTrue(fire_3)
        fire_4 = game.fire_torpedo('second', 'A1')  # fire on same spot hit before, Should be True
        self.assertTrue(fire_4)
        Out_of_turn_test_1 = game.fire_torpedo('second', 'H3')  # OUT OF PLAYER TURN TEST
        self.assertFalse(Out_of_turn_test_1)
        fire_5 = game.fire_torpedo('first', 'B7')  # HIT - TRUE
        self.assertTrue(fire_5)
        fire_6 = game.fire_torpedo('second', 'C2')  # MISS - True
        self.assertTrue(fire_6)
        fire_7 = game.fire_torpedo('first', 'B7')  # FIRE ON previous hit spot - True
        self.assertTrue(fire_7)
        Out_of_turn_test_2 = game.fire_torpedo('first', 'H3')  # OUT OF PLAYER TURN TEST
        self.assertFalse(Out_of_turn_test_2)
        fire_8 = game.fire_torpedo('second', 'C2')  # RE-Fired on previous missed spot - True
        self.assertTrue(fire_8)
        answer = game.get_current_state()
        self.assertEqual(answer, "UNFINISHED")  # Game not finished
        game.fire_torpedo('first', 'C7')
        ships_check = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check, 4)
        ships_check_2 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_2, 5)

        fire_off_grid_1 = game.fire_torpedo('second', 'C12')  # fire off grid should still be true
        self.assertTrue(fire_off_grid_1)
        fire_off_grid = game.fire_torpedo('first', 'Z7')  # fire off grid should still be true
        self.assertTrue(fire_off_grid)

        ships_check_12 = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_12, 4)
        ships_check_13 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_13, 5)

        game.fire_torpedo('second', 'A2')
        game.fire_torpedo('first', 'C2')
        game.fire_torpedo('second', 'A3')
        game.fire_torpedo('first', 'D2')
        game.fire_torpedo('second', 'A4')
        game.fire_torpedo('first', 'E2')
        game.fire_torpedo('second', 'A5')
        ships_check_3 = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_3, 4)
        ships_check_4 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_4, 4)

        game.fire_torpedo('first', 'F2')
        game.fire_torpedo('second', 'B7')
        game.fire_torpedo('first', 'G2')  # player 1 sunk another player 2 ship
        ships_check_23 = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_23, 3)
        ships_check_43 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_43, 4)

        game.fire_torpedo('second', 'C7')
        game.fire_torpedo('first', 'G3')
        game.fire_torpedo('second', 'D7')

        game.fire_torpedo('first', 'G4')
        game.fire_torpedo('second', 'E7')  # player 2 sunk another player 1 ship
        game.fire_torpedo('first', 'G5')
        game.fire_torpedo('second', 'H10')
        game.fire_torpedo('first', 'G6')
        game.fire_torpedo('second', 'I10')  # player 2 sunk another ship
        game.fire_torpedo('first', 'G7')  # player 1 sunk another ship

        ships_check_5 = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_5, 2)
        ships_check_6 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_6, 2)
        answer = game.get_current_state()
        self.assertEqual(answer, "UNFINISHED")  # Game not finished

        game.fire_torpedo('second', 'G2')
        game.fire_torpedo('first', 'H4')
        game.fire_torpedo('second', 'G3')
        game.fire_torpedo('first', 'I4')
        game.fire_torpedo('second', 'G4')  # player 2 sunk another ship
        game.fire_torpedo('first', 'J4')  # player 1 sunk another ship

        ships_check_5 = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_5, 1)
        ships_check_6 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_6, 1)

        game.fire_torpedo('second', 'J4')
        game.fire_torpedo('first', 'C10')
        game.fire_torpedo('second', 'J5')
        game.fire_torpedo('first', 'D10')
        game.fire_torpedo('second', 'J6')
        game.fire_torpedo('first', 'E10')
        game.fire_torpedo('second', 'J6')  # SECOND PLAYER MISSES THE GAME WINNER
        game_over_move = game.fire_torpedo('first', 'F10')  # PLAYER ONE WINS
        false_move_1 = game.fire_torpedo('second', 'J7')  # FALSE MOVE
        false_move_2 = game.fire_torpedo('first', 'E10')  # FALSE MOVE

        # ending checks
        self.assertTrue(game_over_move)
        self.assertFalse(false_move_1)
        self.assertFalse(false_move_2)
        answer = game.get_current_state()
        self.assertEqual(answer, "FIRST_WON")  # Game finished
        ships_check_final_second = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_final_second, 0)
        ships_check_final_first = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_final_first, 1)

    def test_9(self):
        """checking if ship can be whole row and column."""
        game = ShipGame()
        place_ship_1 = game.place_ship('first', 10, 'A1', 'R')
        self.assertTrue(place_ship_1)
        place_ship_2 = game.place_ship('second', 10, 'A1', 'C')
        self.assertTrue(place_ship_2)
        place_ship_3 = game.place_ship('first', 10, 'A1', 'C')
        self.assertFalse(place_ship_3)
        place_ship_4 = game.place_ship('second', 10, 'A1', 'R')
        self.assertFalse(place_ship_4)

    def test_10(self):
        """edge of the board testing for player 1"""

        game = ShipGame()
        place_ship_1 = game.place_ship('first', 5, 'A10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'B10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'C10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'D10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'E10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'F10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'G10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'H10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'I10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'J10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'K10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'J1', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'J2', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'J3', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'J4', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'J5', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'J6', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'J7', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'J8', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'J9', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'J10', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('first', 5, 'J11', 'C')
        self.assertFalse(place_ship_1)

    def test_11(self):
        """edge of the board testing for player 2 """

        game = ShipGame()
        place_ship_1 = game.place_ship('second', 5, 'A10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'B10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'C10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'D10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'E10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'F10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'G10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'H10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'I10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'J10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'K10', 'R')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'J1', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'J2', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'J3', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'J4', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'J5', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'J6', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'J7', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'J8', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'J9', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'J10', 'C')
        self.assertFalse(place_ship_1)
        place_ship_1 = game.place_ship('second', 5, 'J11', 'C')
        self.assertFalse(place_ship_1)

    def test_17(self):
        """testing for hits and wins"""
        game = ShipGame()
        game.place_ship('first', 4, 'A4', 'R')
        game.place_ship('second', 3, 'A9', 'C')
        game.place_ship('first', 4, 'F1', 'C')
        game.place_ship('second', 3, 'D5', 'C')
        game.place_ship('first', 3, 'I5', 'R')
        game.place_ship('second', 3, 'G7', 'R')

        # PLayer 1 - 3 ships ,   PLayer 2 - 3 ships
        ships_check = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check, 3)
        ships_check_2 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_2, 3)

        game.fire_torpedo('first', 'A9')
        game.fire_torpedo('second', 'A4')
        game.fire_torpedo('first', 'B9')
        game.fire_torpedo('second', 'A5')
        game.fire_torpedo('first', 'C9')
        game.fire_torpedo('second', 'A6')
        game.fire_torpedo('first', 'D9')
        game.fire_torpedo('second', 'A7')
        ships_check_3 = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_3, 2)
        ships_check_4 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_4, 2)

        game.fire_torpedo('first', 'D5')
        game.fire_torpedo('second', 'F1')
        game.fire_torpedo('first', 'E5')
        game.fire_torpedo('second', 'G1')
        game.fire_torpedo('first', 'F5')
        game.fire_torpedo('second', 'H1')
        game.fire_torpedo('first', 'F5')
        game.fire_torpedo('second', 'I1')

        ships_check_4 = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_4, 1)
        ships_check_5 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_5, 1)
        answer = game.get_current_state()
        self.assertEqual(answer, "UNFINISHED")  # Game not finished

        game.fire_torpedo('first', 'G7')
        game.fire_torpedo('second', 'I5')
        game.fire_torpedo('first', 'G8')
        game.fire_torpedo('second', 'I6')
        game.fire_torpedo('first', 'G9')
        answer_2 = game.fire_torpedo('second', 'I7')

        ships_check_4 = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_4, 0)
        ships_check_5 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_5, 1)
        answer = game.get_current_state()
        self.assertEqual(answer, "FIRST_WON")
        self.assertFalse(answer_2)

    def test_18(self):
        """ship is less than 2 length"""
        game = ShipGame()
        answer = game.place_ship('first', 1, 'A4', 'R')
        answer_2 = game.place_ship('second', 1, 'A9', 'C')
        self.assertFalse(answer)
        self.assertFalse(answer_2)
        answer_3 = game.place_ship('first', 2, 'A4', 'R')
        answer_4 = game.place_ship('second', 2, 'A9', 'C')
        self.assertTrue(answer_3)
        self.assertTrue(answer_4)

    def test_19(self):
        """testing for hits and wins"""
        game = ShipGame()
        one = game.place_ship('first', 4, 'C4', 'C')
        two = game.place_ship('second', 3, 'D5', 'C')
        false_1 = game.place_ship('first', 5, 'E2', 'R')
        false_2 = game.place_ship('second', 3, 'E3', 'R')
        self.assertTrue(one)
        self.assertTrue(two)
        self.assertFalse(false_1)
        self.assertFalse(false_2)

        ships_check_4 = game.get_num_ships_remaining('second')
        self.assertEqual(ships_check_4, 1)
        ships_check_5 = game.get_num_ships_remaining('first')
        self.assertEqual(ships_check_5, 1)

if __name__ == '__main__':
    unittest.main()
