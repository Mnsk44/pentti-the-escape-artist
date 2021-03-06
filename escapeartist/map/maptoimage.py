"""
utility to convert Map objects into representable images
"""
from typing import List

from PIL import Image

from map.map import Map
from util.constants import BLOCK, EXIT, PENTTI, SPACE, START, VICTORY, VISITED


class MapToImage:

    def __init__(self) -> None:
        self._colors = {
            BLOCK: (0, 0, 0),
            EXIT: (0, 255, 0),
            VISITED: (255, 0 ,0),
            SPACE: (255, 255, 255),
            PENTTI: (255, 0, 255),
            VICTORY: (255, 255, 0),
            START: (0, 255, 255),
        }

    def convert(self, maps: List[Map]) -> Image:
        self._images = [self.to_image(map) for map in maps]

    def to_image(self, map: Map) -> Image:
        colored_map = [self._colors[square] for column in map._map for square in column]
        height, width = map._size

        im = Image.new("RGB", (width, height))
        im.putdata(colored_map)
        return im

    def save_last_png(self, path = "./solution.png"):
        self._images[-1].save(path, format="png")

    def save_images_as_gif(self):
        self._images[0].save(
            "solution.gif",
            save_all=True,
            append_images=self._images[1:],
            duration=50,
        )
