import sys
from pathlib import Path

# Screen Settings
WINDOW_TITLE = "Game Maker"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720  # 20

# Main Setup
FPS = 60
TILE_SIZE = 64
SCREEN_FILL = 'white'

# Menu
MENU_BG = 'SILVER'
MENU_COLS = 2
MENU_ROWS = 3
MENU_MARGIN = 1
MENU_SPACING = 16
MENU_ITEMS = ["terrain", "player", "objects"]
MENU_HL_COLOR = 'gold'
MENU_HL_ALPHA = 100

# Tiles Creator
OVERRIDE_CELL = True

# Assets Path
if getattr(sys, 'frozen', False):
    _asset_path = Path(sys.executable).parent / 'assets'
else:
    _asset_path = Path(__file__).parents[1] / 'assets'
TILES_PATH = _asset_path / 'graphics'

# Grid
GRID = True
GRID_COLOR = (13, 16, 23)
GRID_COLOR_KEY = 'green'
GRID_ALPHA = 50

# Font
FONT = 'Arial'
FONT_SIZE = 15

# Debug
DEBUG = True
DEBUG_COLOR = 'red'
DEBUG_SIZE = 10
DEBUG_BG = (255, 255, 255)
