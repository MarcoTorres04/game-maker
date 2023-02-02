import settings
from menu.tile_surface import TileSurface
from pygame.image import load


class MenuImages:
    def __init__(self):
        self.menu_images: dict[str, dict] = {}
        self.load_images()

    def load_images(self):
        for menu in settings.MENU_ITEMS:
            path = settings.TILES_PATH / menu
            if not menu in self.menu_images:
                self.menu_images[menu]: dict = {}
            for file in path.glob('*.png'):
                image_name = file.stem.split('-')
                if len(image_name) > 1:
                    name, place = image_name
                else:
                    name = image_name[0]
                    place = 'top'
                if not name in self.menu_images[menu]:
                    self.menu_images[menu][name] = {}
                self.menu_images[menu][name][place] = TileSurface(
                    load(str(file)), f"{menu}-{name}-{place}")

    def __call__(self, menu: str, alt: bool = False) -> list:
        if not menu in self.menu_images:
            return []
        images: dict = self.menu_images[menu]
        images_list = list()
        for value in images.values():
            if 'top' in value:
                images_list.append(value['top'])
            elif 'middle' in value:
                images_list.append(value['middle'])
            elif 'bottom' in value:
                images_list.append(value['bottom'])
        return images_list
