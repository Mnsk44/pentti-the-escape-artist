"""
CLI entry point for the maze solver.
"""

import argparse

from character.bfspentti import BFSPentti
from character.randompentti import RandomPentti
from character.righthandpentti import RightHandPentti
from character.usablepentti import UsablePentti
from map.map import Map
from map.maptoimage import MapToImage


parser = argparse.ArgumentParser(description="CLI to helping Pentti escape his doom.")
parser.add_argument(
    "-m",
    "--map",
    type=str,
    required=True,
    dest="map",
    help="Path to a map text file",
)
parser.add_argument(
    "-p",
    "--pentti",
    required=True,
    choices=["random", "righthandrule", "bfs"],
    dest="pentti",
    help="Which solving algorithm to use",
)
parser.add_argument(
    "-l",
    "--limit",
    required=False,
    type=int,
    dest="limit",
    help="Limit Pentti's available moves",
    default=1000,
)
parser.add_argument(
    "-i",
    "--image",
    action="store_true",
    dest="image",
    help="Prints the solution as 'solution.png'"
)
parser.add_argument(
    "-g",
    "--gif",
    action="store_true",
    dest="gif",
    help="Prints the solution steps as 'solution.gif'"
)

if __name__ == "__main__":
    args = parser.parse_args()

    pentti: UsablePentti = None
    map = Map(args.map)

    if args.pentti == "random":
        pentti = RandomPentti(map)
    if args.pentti == "righthandrule":
        pentti = RightHandPentti(map)
    if args.pentti == "bfs":
        pentti = BFSPentti(map)

    pentti.escape_maze(args.limit)

    if args.gif:
        maptoimage = MapToImage()
        maptoimage.convert(pentti._history)
        maptoimage.save_images_as_gif()

    if args.image:
        maptoimage = MapToImage()
        maptoimage.convert([pentti._map])
        maptoimage.save_last_png()
