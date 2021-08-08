"""
Basic layout for dash app
"""
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

centerall = {
    "display": "flex",
    "justify-content": "center",
    "align-items": "center",
    "text-align": "center",
}

layout = html.Div([
    dbc.Navbar(
        html.H1("Pentti the Escape Artist"),
        style=centerall,
    ),
    html.Div(
        html.P(
        "Pentti is stuck in a maze! You can help him escape, but how much will you help?"
        ),
        style=centerall,
    ),
    html.Div(
        [
            html.H3("Choose your mood: ")
        ],
        style=centerall
    ),
    html.Div([
        dbc.Button("Evil", id="evil-btn", className="mr-1"),
        dbc.Button("Neutral", id="neutral-btn", className="mr-1"),
        dbc.Button("Good", id="good-btn", className="mr-1"),
        ],
        style=centerall,
    ),
    html.Div(
        [
            html.P("You may limit Pentti's steps:"),
            dcc.Input(id="limit-input", type='number', value=200)
        ],
        style=centerall,
    ),
    html.Div(id="result-div-evil-text", style=centerall),
    html.Div(id="result-div-evil-png", style=centerall),
    html.Div(id="result-div-neutral-text", style=centerall),
    html.Div(id="result-div-neutral-png", style=centerall),
    html.Div(id="result-div-good-text", style=centerall),
    html.Div(id="result-div-good-png", style=centerall),
])
