"""
Entry point for World data visualization app
"""
import server.callbacks
from server.app import app
from server.layout import layout


app.layout = layout

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8080)