"""
CLI entry point for the maze solver.
"""

import argparse
from character.pentti import Pentti

from map.map import Map
from character.randompentti import RandomPentti
from character.righthandpentti import RightHandPentti

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
    choices=["random", "righthandrule"],
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

if __name__ == "__main__":
    args = parser.parse_args()

    pentti: Pentti = None
    map = Map(args.map)

    if args.pentti == "random":
        pentti = RandomPentti(map)
        pentti.random_escape(args.limit)
    if args.pentti == "righthandrule":
        pentti = RightHandPentti(map)
        pentti.right_hand_escape(args.limit)
