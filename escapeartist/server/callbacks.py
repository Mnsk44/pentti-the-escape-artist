"""
Callbacks for dash app
"""

import base64
from io import BytesIO

from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

from character.bfspentti import BFSPentti
from character.randompentti import RandomPentti
from character.righthandpentti import RightHandPentti
from map.map import Map
from map.maptoimage import MapToImage
from server.app import app
from util.constants import VICTORY



@app.callback(
    [Output("result-div-evil-text", "children"), Output("result-div-evil-png", "children")],
    [Input("evil-btn", "n_clicks")],
    [State("limit-input", "value"), State("map-dropdown", "value")],
    prevent_initial_call=True
)
def evil_random_escape(click, limit, map_path):
    map = Map(map_path)
    pentti = RandomPentti(map)
    pentti.escape_maze(limit)
    if pentti._map[pentti.position()] == VICTORY:
        result = f"Pentti escaped in {len(pentti._history)} steps"
    else:
        result = f"Pentti was exhausted after {limit} steps, Pentti did not escape..."
    text = html.P(
        "You have chosen to not give Pentti any instructions :( he wanders randomly in the maze... "
        + result
    )

    maptoimage = MapToImage()

    maptoimage.convert([pentti._map])

    # This is adapted from
    # https://stackoverflow.com/questions/60712647/displaying-pil-images-in-dash-plotly
    buffer = BytesIO()
    maptoimage.save_last_png(buffer)
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")

    im = html.Img(
        className="image",
        src="data:image/png;base64, " + encoded, style={"height":"35%", "width":"35%"}
    )

    return text, im


@app.callback(
    [Output("result-div-neutral-text", "children"), Output("result-div-neutral-png", "children")],
    [Input("neutral-btn", "n_clicks")],
    [State("limit-input", "value"), State("map-dropdown", "value")],
    prevent_initial_call=True
)
def right_hand_escape(click, limit, map_path):
    map = Map(map_path)
    pentti = RightHandPentti(map)
    pentti.escape_maze(limit)
    if pentti._map[pentti.position()] == VICTORY:
        result = f"Pentti escaped in {len(pentti._history)} steps"
    else:
        result = f"Pentti was exhausted after {limit} steps, Pentti did not escape..."
    text = html.P(
        "You have chosen to instruct Pentti to keep his right hand touching a wall at all times... "
        + result
    )

    maptoimage = MapToImage()

    maptoimage.convert([pentti._map])

    # This is adapted from
    # https://stackoverflow.com/questions/60712647/displaying-pil-images-in-dash-plotly
    buffer = BytesIO()
    maptoimage.save_last_png(buffer)
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")

    im = html.Img(
        className="image",
        src="data:image/png;base64, " + encoded, style={"height":"35%", "width":"35%"}
    )

    return text, im


@app.callback(
    [Output("result-div-good-text", "children"), Output("result-div-good-png", "children")],
    [Input("good-btn", "n_clicks")],
    [State("limit-input", "value"), State("map-dropdown", "value")],
    prevent_initial_call=True
)
def bfs_escape(click, limit, map_path):
    map = Map(map_path)
    pentti = BFSPentti(map)
    pentti.escape_maze(limit)
    if pentti._count_path_length() < limit:
        result = f"Pentti escaped in {pentti._count_path_length()} steps"
    else:
        result = f"Pentti was exhausted after {limit} steps, Pentti did not escape..."
    text = html.P(
        "You have chosen to give a map to Pentti! Pentti will look for a good route to escape! "
        + result
    )

    maptoimage = MapToImage()

    maptoimage.convert([pentti._map])

    # This is adapted from
    # https://stackoverflow.com/questions/60712647/displaying-pil-images-in-dash-plotly
    buffer = BytesIO()
    maptoimage.save_last_png(buffer)
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")

    im = html.Img(
        className="image",
        src="data:image/png;base64, " + encoded, style={"height":"35%", "width":"35%"}
    )

    return text, im