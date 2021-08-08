# Pentti, the Escape Artist
---

Pentti needs to get to the other side of the maze, but he doesn't know how!

You, as an omnipotent deity, can choose to help Pentti in the way you choose; are you giving him hints on how to escape the maze or are you giving the map to his hands? You decide!

---

TL;DR; A short python project testing different maze solving algorithms.

---

Run the CLI with `escapeartist/main.py`
```bash
usage: main.py [-h] -m MAP -p {random,righthandrule,bfs} [-l LIMIT] [-i] [-g]

CLI to helping Pentti escape his doom.

optional arguments:
  -h, --help            show this help message and exit
  -m MAP, --map MAP     Path to a map text file
  -p {random,righthandrule,bfs}, --pentti {random,righthandrule,bfs}
                        Which solving algorithm to use
  -l LIMIT, --limit LIMIT
                        Limit Pentti's available moves
  -i, --image           Prints the solution as 'solution.png'
  -g, --gif             Prints the solution steps as 'solution.gif'
```