import sys
from pathlib import Path

# Screen Settings
WINDOW_TITLE = "Game Maker"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720  # 20

# Main Setup
FPS = 60
TILE_SIZE = 64
SCREEN_FILL = 'SKYBLUE'

# Menu
MENU_BG = 'SILVER'
MENU_COLS = 2
MENU_ROWS = 3
MENU_MARGIN = 1
MENU_SPACING = 16
MENU_ITEMS = ["tiles", "players", "objects"]
MENU_HL_COLOR = 'gold'
MENU_HL_ALPHA = 100
SCROLL_SENS = 1

# Tiles Creator
OVERRIDE_CELL = True

# Assets Path
if getattr(sys, 'frozen', False):
    _asset_path = Path(sys.executable).parent / 'assets'
else:
    _asset_path = Path(__file__).parents[1] / 'assets'
TILES_PATH = _asset_path / 'graphics'

TILES_BG = (0, 85, 115)
PLAYER_BG = (94, 195, 224)

# Grid
GRID = True
GRID_COLOR = (13, 16, 23)
GRID_COLOR_KEY = 'green'
GRID_ALPHA = 50

# Font
FONT = 'Arial'
FONT_SIZE = 15

# Player Stats
PLAYER_SPEED = 18
PLAYER_GRAVITY = 0.5
PLAYER_JUMP = 3.1
CAMERA_MODE = "center"  # "center" | "box"
CAMERA_BOX = {
    "top": 400,
    "left": 400,
    "width": 1000,
    "height": 500
}
PLAYER_ANIMATION_SPEED = 0.3

# Game Ui
PLAY_UI_BG = "black"
PLAY_UI_FONT_COLOR = "white"

# Screen Animiation
ANIMATION_SPEED = 25
ANIMATION_COLOR = (11, 14, 20)

# Start Menu
START_MENU_BG = (0, 87, 132)
START_MENU_TITLE_COLORS = ['crimson', 'orangered', 'coral', 'salmon', 'red']
START_MENU_SPEED = 0.02
START_MENU_FONTSIZE = 35

# Debug
DEBUG = False
DEBUG_COLOR = 'red'
DEBUG_SIZE = 10
DEBUG_BG = (255, 255, 255)

DEAD_LEVEL = 10
DEAD_LEVEL_COLOR = 'red'
SHOW_DEAD_LEVEL = True
