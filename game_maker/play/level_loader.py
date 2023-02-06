import json
import typing

import pygame as pg
import settings
from pygame.image import load as load_image

if typing.TYPE_CHECKING:
    from .level import Level

from .animated_player import AnimatedPlayer
from .player import Player
from .tile import LevelTile


class LevelLoader:
    def __init__(self):
        self.display_surface = pg.display.get_surface()

    def __call__(self, level: 'Level', canvas: dict[tuple[int, int], str]) -> Player:
        metadatas = {}
        images_path = settings.TILES_PATH
        player = None

        for loc, path in canvas.items():
            menu, name, place = path.split('-')
            pos = loc[0] * settings.TILE_SIZE, loc[1] * settings.TILE_SIZE

            # Load Metadata File
            metadata_path = images_path / menu / f'{menu}.json'
            if not menu in metadatas and metadata_path.exists():
                with open(metadata_path, 'r') as json_file:
                    metadatas[menu] = json.load(json_file)

            if '_ANIMATION' in place:
                _images = self.get_animated_images(path)
                _metadata = metadatas.get(menu, {}).get(name, {})
                player = AnimatedPlayer(_images, pos, [level.draw_sprites,
                                                       level.update_sprites], level.collision_sprites, _metadata)
                continue

            # Create Tiles
            if (images_path / menu / name).is_dir():
                image_folder = images_path / menu / name
            else:
                image_folder = images_path / menu
            image_path = image_folder / f'{name}-{place}.png'
            if not image_path.exists():
                image_path = image_folder / f'{name}.png'
            # Detect Player
            _metadata = metadatas.get(menu, {}).get(name, {})
            image = load_image(image_path)
            if 'player' in name:
                player = Player(image, pos, [level.draw_sprites,
                                             level.update_sprites], level.collision_sprites, _metadata)
            else:
                LevelTile(image, pos, [level.draw_sprites,
                          level.collision_sprites], _metadata)
        return player

    def get_animated_images(self, path: str) -> dict:
        path = path.replace('_ANIMATION', '')
        animations_folder = settings.TILES_PATH / 'animations' / path
        images = {}
        for state in animations_folder.glob('*'):
            if not state.stem in images:
                images[state.stem] = []
            for image_path in state.glob('*.png'):
                images[state.stem].append(load_image(image_path))
        return images
