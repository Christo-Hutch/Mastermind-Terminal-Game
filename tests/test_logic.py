# External (Python Libraries)
import sys
from pathlib import Path

# Internal (Game Files)
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))
import src.game_logic

# Initialises Game
src.game_logic.Game.initialiseGame()

# Test Board with 5 rows
testBoard = src.game_logic.Board(5)

# Sets a random code maker code
testBoard.setRandomCode()

