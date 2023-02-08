import json
from pathlib import Path

import settings
from pygame.image import load as load_image

from .asset import Asset


class AssetsLoader:
    def __init__(self):
        pass

    def __call__(self) -> dict:
        assets = {}
        graphics_path = settings.TILES_PATH
        assets['players'] = read_player_assets(graphics_path)
        assets['tiles'] = read_asset_folder(graphics_path, 'tiles')
        assets['objects'] = read_asset_folder(graphics_path, 'objects')
        return assets


def read_player_assets(graphics_path: Path) -> dict:
    players = {}
    players_path = graphics_path / 'players'
    players_meta_plath = players_path / 'players.json'
    players['metadata'] = load_metadata(players_meta_plath)

    for player_folder in players_path.glob('*'):
        if not player_folder.is_dir():
            continue
        players[player_folder.stem] = {}
        for player in player_folder.rglob('*.png'):
            state = player.parts[-2]
            if not state in players[player_folder.stem]:
                players[player_folder.stem][state] = []
            players[player_folder.stem][state].append(
                Asset(player, f'players-{player_folder.stem}-{state}', players['metadata'].get(player_folder.stem, {})))
    return players


def read_asset_folder(graphics_path: Path, asset_name: str) -> dict:
    assets = {}
    assets_path = graphics_path / asset_name
    assets_meta_path = assets_path / f'{asset_name}.json'
    assets['metadata'] = load_metadata(assets_meta_path)
    for asset_folder in assets_path.glob('*'):
        if not asset_folder.is_dir():
            continue
        assets[asset_folder.stem] = {}
        for asset in asset_folder.glob('*'):
            state = asset.stem
            _meta = assets['metadata'].get(asset_folder.stem, {})
            # PNG Images
            if asset.is_file():
                if not state in assets[asset_folder.stem]:
                    assets[asset_folder.stem][state] = [Asset(
                        asset, f'{asset_name}-{asset_folder.stem}-{asset.stem}', _meta)]
                continue
            for asset_animation in asset.glob('*.png'):
                if not state in assets[asset_folder.stem]:
                    assets[asset_folder.stem][state] = []
                assets[asset_folder.stem][state].append(
                    Asset(asset_animation, f'{asset_name}-{asset_folder.stem}-{state}', _meta))
    return assets


def load_metadata(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, 'r') as meta_file:
        metadata: dict = json.load(meta_file)
    return metadata
